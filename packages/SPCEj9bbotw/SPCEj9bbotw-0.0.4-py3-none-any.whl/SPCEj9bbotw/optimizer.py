import numpy as np
import numpy.linalg as lg
import cupy as cp
from SPCEj9bbotw._ import *


'''
coefficient matrix of primal variable is calculated by cupy inverse function.
'''
class gpu_optimizer:
    def __init__(self, x_0, n, dt, rho, cond, g, ang_vel, epoch, func_gpu):
        self.x_0 = x_0
        self.n = n
        self.dt = dt
        self.rho = rho
        self.g = g
        self.ang_vel = ang_vel
        self.cond = cond
        self.epoch = np.int32(epoch)
        self.eps_r = 0.001
        self.eps_s = 0.001
        self.scaling()
        self.func_main_ = func_gpu
        # self.make_mtrx/()
        # self.init_gpu()
        # self.func_GPU()
        
        # self.func_main_ = ker_main_(self.n)///
        
        
    def scaling(self):
        scl_pos = 100  
        scl_vel = 10  
        scl_u = 1
        scl_sig = 10
        scl_z = 1
        
        self.scale = {}
        self.scale['x'] = np.diag([scl_pos]*3+[scl_vel]*3)
        self.scale['inv/x'] = lg.inv(self.scale['x'])
        self.scale['u'] = np.diag([scl_u]*3)
        self.scale['inv/u'] = lg.inv(self.scale['u'])
        self.scale['sig'] = scl_sig
        self.scale['inv/sig'] = 1/self.scale['sig']
        self.scale['z'] = scl_z
        self.scale['inv/z'] = 1/self.scale['z']
        
        self.A = np.eye(6)
        matrix.fill_diag(self.A, (self.dt, 3))
        self.tA = self.A.T
        self.B = np.zeros((6,3))
        matrix.fill_diag(self.B, (0.5*self.dt**2,0), (self.dt, -3))
        self.tB = self.B.T       
        
        self.A_scl = self.scale['inv/x']@self.A@self.scale['x']
        self.tA_scl = self.A_scl.T
        self.B_scl = self.scale['inv/x']@self.B@self.scale['u']
        self.tB_scl = self.B_scl.T
        self.g_scl = self.scale['inv/x']@self.B@self.g
        self.cond['alpha_scl'] = self.scale['inv/z']*self.cond['alpha']*self.scale['sig']
        
        self.z_lb_scl = self.scale['inv/z']*np.array([np.log(self.cond['m_0'] - self.cond['alpha']*self.cond['rho2']*
                                                             self.dt*i) for i in range(self.n+1)])
        self.z_ub_scl = self.scale['inv/z']*np.array([np.log(self.cond['m_0'] - self.cond['alpha']*self.cond['rho1']*
                                                             self.dt*i) for i in range(self.n+1)])
        
        
    def make_mtrx(self):
        self.TM = {}      
        self.TM['y2u-sig'] = transformation.extract((4,11), [0,1,2,9], self.n)
        block = np.zeros((2, 2*11))
        block[0, 20] = 1
        block[1,10] = 1
        self.TM['y2sig-z'] = transformation.band(block, self.n, 11)
        self.TM['y2sig-z'] = self.TM['y2sig-z'][:, 11:]
         
            
        ##make alpha##        
        block = np.block([[np.zeros((6,3)), self.A_scl, np.zeros((6,2)), self.B_scl, -np.eye(6), np.zeros((6,2))],
                          [np.zeros(10), np.array([1]), np.zeros(9), np.array([-self.cond['alpha_scl']*self.dt, -1])]])
        self.alpha = transformation.band(block, self.n, 11)
        self.alpha = self.alpha[:,11:]
        self.alpha = sp.csr_array(self.alpha)
        self.talpha = self.alpha.T

        ##beta##     
        self.beta = np.tile(np.hstack((-self.g_scl, [0])), self.n)[:, np.newaxis]
        self.beta[:6,:] = self.beta[:6,:] - self.scale['inv/x']@self.A_scl@self.x_0 
        self.beta[6,:] = -self.scale['inv/z']*np.log(self.cond['m_0'])
        
        #################################################################################################
        ##gamma##
        tmp1 = np.zeros((self.n,1,3))
        tmp1[:,:,-1] = 1
        tmp1 = sparse.block(tmp1, (1,3), self.n)

        tmp2 = np.zeros((self.n,1,3))
        tmp2[:,:,-1] = -1
        tmp2 = sparse.block(tmp2, (1,3), self.n)

        tmp3 = np.zeros((self.n,1,3))
        tmp3[:,:,0] = 1
        tmp3 = sparse.block(tmp3, (1,3), self.n)


        self.gamma = sp.vstack([tmp1, tmp2, tmp3])
        self.gamma = sp.csr_array(self.gamma)@transformation.extract((3,11), [0,9,10], self.n)
        self.tgamma = self.gamma.T
        ###############################################################################################

        ## zeta ##
        self.zeta = np.hstack((self.z_lb_scl[1:], -self.z_ub_scl[1:], np.zeros(self.n)))[:,np.newaxis]

        ## C ##
        self.C = sp.csr_array(sp.vstack([self.gamma, self.TM['y2u-sig'], self.TM['y2sig-z']]))
        self.tC = sp.csr_array(self.C.T)

        
        ##b3
        self.b3 = sp.csr_array((2*self.n, 1))
        self.b3[1] = -np.log(self.cond['m_0'])
        
        # ||xn||^2 - Zn
        self.coeff_y = self.rho*self.C.T@self.C
        self.coeff_y[-8:-2, -8:-2] = self.coeff_y[-8:-2, -8:-2] + sp.csr_array(sp.diags([1000, 100, 100, 10, 1, 1]))
        a = sp.hstack([self.coeff_y, self.talpha])
        b = sp.hstack([self.alpha, sp.csr_array((7*self.n,7*self.n))])
        self.coeff_y = sp.vstack([a,b])
        self.tilde_C_gpu = cp.array(self.coeff_y.toarray().astype(np.float32))
        self.tilde_C_gpu = cp.linalg.inv(self.tilde_C_gpu)
        

        ##fixed matrix for updating y
        h = sp.csr_array((11*self.n,1))
        h[-1] = -1*100
        q_tilde = sp.vstack([self.zeta, sp.csr_array((4*self.n,1)), self.b3])
        self.y_fix = sp.csr_array(sp.vstack([-h + self.rho*self.tC@q_tilde, self.beta]))
        self.y_fix_gpu = self.tilde_C_gpu[:11*self.n, :]@cp.array(self.y_fix.toarray().astype(np.float32))        
        self.tilde_C_gpu = self.tilde_C_gpu[:11*self.n, :11*self.n]@cp.array((self.rho*self.tC).toarray().astype(np.float32))
        
    def init_gpu(self):
        self.y_gpu = cp.array(np.zeros((11*self.n, 1)).astype(np.float32))   
        self.acc_cmd_gpu = cp.array(np.zeros(3).astype(np.float32) , copy=False)
        self.z_lb_gpu = cp.array(self.z_lb_scl.astype(np.float32))
        self.z_ub_gpu = cp.array(self.z_ub_scl.astype(np.float32))
        self.N_gpu = np.int32(self.n)
        
    def admm_main(self):
        self.func_main_((1, 11, 1), (1, self.n, 1), (self.y_gpu,  self.y_fix_gpu, self.tilde_C_gpu, 
                                                     self.z_lb_gpu, self.z_ub_gpu, self.N_gpu, self.epoch, self.acc_cmd_gpu))



def ker_main_(N):
    num_thread = int(11*N)
    str_ = r"""
    #define _X (blockDim.x * blockIdx.x + threadIdx.x)
    #define _Y (blockDim.y * blockIdx.y + threadIdx.y)    
    #define _Coor (_X + _Y*gridDim.x*blockDim.x)
    #include <cooperative_groups.h>
    namespace cg = cooperative_groups;
    
    typedef struct {
        int u;
        int x;
        int sig;
        int z;
    } IDXS;
    
    typedef struct {
        float rho1;
        float rho2;
    } COND;
    
    typedef struct {
        float theta;
        float sig;
        float u;
        float z;
        float pos ;
        float vel ;
        float socb;
        float exp1;
        float exp2;
    } SCALE;


    __device__ float buff_y[""" + repr(num_thread) + r"""] ={0.0} ;

    __device__ float w["""+ repr(num_thread) +r"""]={0.0}  ;

    __device__ float buff_w["""+ repr(num_thread) +r"""]={0.0} ;

    __device__ float buff["""+ repr(num_thread) +r"""]={0.0} ;

    __device__ float ys["""+ repr(num_thread) +r"""] ={0.0};

    __device__ int NR_epoch = 1000;

    __device__ int NR_eps = 0.001;
    
    __device__ SCALE scale ={0, 10, 1, 1, 100, 10, 0.1, 0.1*0.2*24000, 0.1*0.8*24000};
    

    __device__ float NR_f(float x, float a, float b, float rho){

        return expf(x)*(x - a) - powf(rho, 2)*expf(-x) + rho*(b);
    }

    __device__ float NR_fdot(float x, float a, float b, float rho){

        return expf(x)*(x - a + 1) + powf(rho, 2)*expf(-x);
    }

    __device__ float func_matmulvec(float* x, float* y, int act_len){

        float result = 0;

        for(int i=0; i < act_len; i++){
            result += x[i]*y[i];
        }

        return result;
    }

    __device__ float func_norm(float* ptr){

        float norm=0;

        for(int i=0; i < 3; i++){
            norm += ptr[i]*ptr[i];
        }

        return sqrt(norm);
    }

    __device__ void proj_lb(float* x, float lb){

        if(*x < lb){
            *x = lb;
        }
    }

    __device__ void Gcone_(float* u, float* sig, float t){

        float norm = func_norm(u);

        if(*sig <= -1/t*norm && *sig < 0){
            *sig = 0;
            for(int i=0; i<3; i++){
                u[i] = 0;
            }
        }
        else if(norm != 0){

            float temp = (norm + (*sig)*t)/(1+powf(t,2));

            for(int i=0; i<3; i++){
                u[i] = (temp/norm)*u[i];
                *sig = temp*t;
            }
        }

    }
    
    
    
    __device__ float NR(float* a, float* b, float rho){

        float x = *a;
        
        for(int i=0; i < NR_epoch; i++){
            x = x - NR_f(x, *a, *b, rho)/NR_fdot(x, *a, *b, rho);
            if(fabsf(NR_f(x, *a, *b, rho)) <= NR_eps){
                return x;
            }
        }

        return x;
    }

    __device__ void itv_exp(float* sig, float* z, float rho1, float rho2){

        if(*sig < rho1*expf(- *z)){
            *z = NR(z, sig, rho1);
            *sig = rho1*expf(- *z);



        }
        else if(*sig > rho2*expf(- *z)){
            *z = NR(z, sig, rho2);
            *sig = rho2*expf(- *z);

            
        }

    }


    extern "C"
    __global__ void main_(float* y, float* y_fix, float* tilde_C, float* z_lb, float* z_ub, int N, int epoch, float* acc_cmd){

        int idx = _Coor;
        int len_var = 11*N;
        int len_dual = 9*N;
        int shr_idx = idx % 11;
        int res_idx = idx % N;
        
        SCALE scale;

        IDXS idxs;
        idxs.u = 11*idx; idxs.x = 11*idx+3; idxs.sig = 11*idx+9; idxs.z = 11*idx+10;

        IDXS res_idxs;
        res_idxs.u = 11*res_idx; res_idxs.x = 11*res_idx+3; res_idxs.sig = 11*res_idx+9; res_idxs.z = 11*res_idx+10;
        
        float* th_proj1;
        float* th_proj2;
        float* th_ys;

        cg::grid_group grid = cg::this_grid();
        
        buff[idx] = 0;
        buff_w[idx] = 0;
        ys[idx] = 0;
        w[idx] = 0;
        
        sync(grid);

        /*-----------------------------------------------------------------*/
        
        if(idx < 3*N){
            float a = 3;
        }
        else if(3*N <= idx && idx < 4*N){
            th_proj1 = &buff_w[3*N+res_idx*4];   // u
            th_proj2 = &buff_w[3*N+res_idx*4+3]; // sig
            th_ys = &ys[3*N+res_idx*4];
        }
        else if(4*N <= idx && idx < 5*N){ //projection for exponential inequality
            th_proj1 = &buff_w[7*N+res_idx*2];   // sig
            th_proj2 = &buff_w[7*N+res_idx*2+1]; // z
            th_ys = &ys[7*N+res_idx*2];
            
        }

        /*-----------------------------------------------------------------*/
        for(int iter_=0; iter_ < epoch; iter_++){
            if(idx < len_dual){
                buff[idx] = w[idx] - ys[idx];
            }
            sync(grid);
                
            
            buff_y[idx] = y_fix[idx] + func_matmulvec(&tilde_C[len_dual*idx], buff, len_dual);
        
            sync(grid);

            /*-----------------projection--------------------------------------*/

            /*-----------------linear inequality--------------------------------------------*/
            
            if(idx < N){
                buff_w[idx] = buff_y[res_idxs.z] - z_lb[res_idx+1] + ys[idx];
                proj_lb(&buff_w[idx], 0);
                ys[idx] = ys[idx] + buff_y[res_idxs.z] -z_lb[res_idx+1] - buff_w[idx];   
            }
            else if(N <= idx && idx < 2*N){
                buff_w[idx] = - buff_y[res_idxs.z]  + z_ub[res_idx+1] + ys[idx];
                proj_lb(&buff_w[idx], 0);
                ys[idx] = ys[idx]  -buff_y[res_idxs.z] +z_ub[res_idx+1] - buff_w[idx];
            }
            else if(2*N <= idx && idx < 3*N){
                buff_w[idx] = buff_y[res_idxs.u] - 0*buff_y[res_idxs.sig] + ys[idx];
                proj_lb(&buff_w[idx], 0);
                ys[idx] = ys[idx] + buff_y[res_idxs.u] - 0*buff_y[res_idxs.sig] - buff_w[idx];
            }

            /*-----------------socbp----------------------------------*/
            else if(3*N <= idx && idx < 4*N){
                for(int i=0; i < 3; i++){
                    th_proj1[i] = buff_y[res_idxs.u+i] + th_ys[i];
                }
                *th_proj2 = buff_y[res_idxs.sig] + th_ys[3];
                //Gcone_(th_proj1, th_proj2, scale.socb);
                Gcone_(th_proj1, th_proj2, 0.1);
                
                for(int i=0; i < 3; i++){
                    th_ys[i] = th_ys[i] + buff_y[res_idxs.u+i] - th_proj1[i];
                }
                th_ys[3] = th_ys[3] + buff_y[res_idxs.sig] - *th_proj2;
                

            }
           
            else if(4*N <= idx && idx <5*N){
                if(res_idx == 0){
                    *th_proj1 = buff_y[res_idxs.sig] + th_ys[0];
                    *th_proj2 = z_lb[0] + th_ys[1];
       
                }
                else{
                    *th_proj1 = buff_y[res_idxs.sig] + th_ys[0];
                    *th_proj2 = buff_y[res_idxs.z-11] + th_ys[1];
     
                }
                itv_exp(th_proj1, th_proj2, 480, 1920);
                
                
                if(res_idx == 0){
                    th_ys[0] = th_ys[0] + buff_y[res_idxs.sig] - *th_proj1;
                    th_ys[1] = th_ys[1] + z_lb[0] - *th_proj2;
        
                }
                else{
                    th_ys[0] = th_ys[0] + buff_y[res_idxs.sig] - *th_proj1;
                    th_ys[1] = th_ys[1] + buff_y[res_idxs.z-11] - *th_proj2;
                    
                }
                
            }
            sync(grid);
            
            y[idx] = buff_y[idx];
            w[idx] = buff_w[idx];
            sync(grid);  
        }
        //y[idx] = buff_w[idx];
        sync(grid);
        if(idx == 0){
            for(int i=0; i < 3; i++){
                acc_cmd[i] = y[i];
            }
        }

        sync(grid);
    }
    """
    SM_main_ = cp.RawKernel(str_, 'main_', enable_cooperative_groups=True)
    return SM_main_

       

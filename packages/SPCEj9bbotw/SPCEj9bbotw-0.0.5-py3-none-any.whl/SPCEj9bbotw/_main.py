import numpy as np
import numpy.linalg as lg
import cupy as cp
# from SPCEj9bbotw.kernels import *
# from SPCEj9bbotw.optimizer import *
from optimizer import gpu_optimizer
from kernels import ker_main_
import time
import matplotlib.pyplot as plt

def plot(optimizer):
    y = cp.asnumpy(optimizer.y_gpu)
    # print(type(optimizer.y_gpu))
    u = optimizer.scale['u']@(y.reshape(-1,11)[:,:3]).T
    z = optimizer.scale['z']*y.reshape(-1,11)[:,-1]

    z = z.reshape(-1)

    z = np.hstack(([np.log(optimizer.cond['m_0'])],z))
    norm_u = lg.norm(u, axis=0)
    mass = np.exp(z[:-1])
    throttle = norm_u*mass
    print(throttle)
    print(optimizer.scale['inv/sig']*optimizer.cond['rho1'],  optimizer.scale['inv/sig']*optimizer.cond['rho2'])

    database = optimizer
    obj_admm = database

    x = obj_admm.scale['x']@(y.reshape((-1, 11))[:,3:9]).T

    print(x[:,-1])
    x = np.hstack((obj_admm.x_0, x))
    u = obj_admm.scale['u']@(y.reshape(-1,11)[:,:3]).T
    sigma = obj_admm.scale['sig']*y.reshape(-1,11)[:,-2]
    z = obj_admm.scale['z']*y.reshape(-1,11)[:,-1]

    z = z.reshape(-1)

    z = np.hstack(([np.log(database.cond['m_0'])],z))


    print(optimizer.z_lb_scl[0], optimizer.scale['inv/z']*np.log(optimizer.cond['m_0']))
    norm_u = lg.norm(u, axis=0)
    mass = np.exp(z[:-1])
    throttle = norm_u*mass
    theta = np.rad2deg(np.arccos(u[0,:]/norm_u))
    print(throttle)

    fig, axes = plt.subplots(3,3, figsize=(16,16))
    axes[0,0].plot(theta, label=r'$\theta$')
    axes[0,0].plot([np.rad2deg(obj_admm.cond['theta'])]*obj_admm.n, label=u'90\N{DEGREE SIGN}')
    axes[0,0].legend()

    axes[0,1].plot([obj_admm.cond['rho1']]*obj_admm.n)
    axes[0,1].plot([obj_admm.cond['rho2']]*obj_admm.n)
    axes[0,1].plot(throttle, label='throttle')
    axes[0,1].legend()

    axes[0,2].plot(x[1,:], x[2,:])
    axes[0,2].plot(0, 0, '*')
    axes[0,2].set_xlabel('Y(m)')
    axes[0,2].set_ylabel('Z(m)')
    axes[0,2].set_title('Surface Tragectory')


    axes[1,0].plot(obj_admm.scale['z']*obj_admm.z_lb_scl, label='lb')
    axes[1,0].plot(obj_admm.scale['z']*obj_admm.z_ub_scl, label='ub')
    axes[1,0].plot(z, label='z')
    axes[1,0].legend()


    axes[1,1].plot(sigma, label='sigma', alpha=0.1,  linewidth='10')
    axes[1,1].plot(norm_u, label='||u||')
    axes[1,1].legend()

    axes[1,2].plot(obj_admm.cond['rho1']*np.exp(-z), label='lb')
    axes[1,2].plot(obj_admm.cond['rho2']*np.exp(-z), label='ub')
    axes[1,2].plot(sigma, label='sigma')
    axes[1,2].legend()

    axes[2,0].plot(np.cos(obj_admm.cond['theta'])*sigma, label=r'$\cos90^{\degree}\sigma$')
    axes[2,0].plot(u[0,:], label=r'$u_{0}$')
    axes[2,0].legend()

    axes[2,1].plot(np.hstack((z[0], z[:-1]-obj_admm.cond['alpha']*obj_admm.dt*sigma)), linewidth='10', alpha=0.1, label='dynamic')
    axes[2,1].plot(z, label='opt_z')
    axes[2,1].legend()
    axes[2,1].set_title(r'$\sigma - z \ dynamics$')

    dynamic_x = obj_admm.A@x[:,:-1]+obj_admm.B@(np.array(obj_admm.g)[:,np.newaxis]+u)
    dynamic_x = np.hstack((obj_admm.x_0, dynamic_x))
    axes[2,2].plot(x[1,:], label='px')
    axes[2,2].plot(dynamic_x[1, :], linewidth='10', alpha=0.1, label='dynamic')
    axes[2,2].legend()
    axes[2,2].set_title(r'$x \ dynamics$')


    print('required fuel', np.exp(z[0]) - np.exp(z[-1]))
    plt.show()


x_0 =np.array([2, 2, 1.5, -0.3, 0, 0])[:,np.newaxis]
x_des = np.zeros(6)
n = 50
dt = 0.1

init_cond = {'m_0': 0.03, 'm_f': 0.003, 'rho1': 9.5*0.03, 'rho2': 9.9*0.03, 'T_max': 24000, 'alpha': 5e-9, 
            'theta': np.deg2rad(90)}
g = np.array([-9.81, 0, 0])

scl_pos = 1
scl_vel = 1
scl_u = 1
scl_sig = 10
scl_z = 0.1

ang_vel = [0,0,0]
acc_cmd = np.zeros(3)
mempool = cp.get_default_memory_pool()

stream = cp.cuda.Stream()
func_gpu = ker_main_(n)



for i in range(20):

    optimizer = gpu_optimizer(x_0, n, dt, 20, init_cond, g, ang_vel, 2000, func_gpu)
    optimizer.scaling((scl_pos, scl_vel, scl_u, scl_sig, scl_z))
    optimizer.make_mtrx()
    optimizer.init_gpu()
    optimizer.admm_main()
    acc_cmd = cp.asnumpy(optimizer.acc_cmd_gpu)[:,np.newaxis]
    acc_cmd[:3,:] = optimizer.scale['u']@acc_cmd[:3,:]
    acc_cmd[-1,:] = optimizer.scale['sig']*acc_cmd[-1,:]
    
    
    x_0 = optimizer.A@x_0 + optimizer.B@(acc_cmd[:3,:] + g[:,np.newaxis])
    init_cond['m_0'] = np.exp(np.log(init_cond['m_0']) - init_cond['alpha']*dt*acc_cmd[-1,0])
    n = n-1
    print('start', x_0)
    # print(i, n, x_0, init_cond['m_0'])
    # print(acc_cmd)
plot(optimizer)
    # a = input('')
    

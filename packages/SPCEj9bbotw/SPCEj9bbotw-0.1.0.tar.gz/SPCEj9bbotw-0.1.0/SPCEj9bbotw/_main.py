import numpy as np
import numpy.linalg as lg
import cupy as cp
from functions._plot import plot
from optimizer import ker_main_, gpu_optimizer
import time
import matplotlib.pyplot as plt


'''
state update & guidance loop
'''

x_0 =np.array([2, 2, 1.5, 0, 0, 0])[:,np.newaxis]
# x_0 =np.array([2.196, 1.906, 1.881, -0.0620, 0, 0])[:,np.newais]

x_des = np.zeros(6)
n = 50
dt = 0.1

init_cond = {'m_0': 0.03, 'm_f': 0.003, 'rho1': 9.5*0.03, 'rho2': 9.9*0.03, 'T_max': 24000, 'alpha': 5e-9, 
            'theta': np.deg2rad(20)}
g = np.array([-9.81, 0, 0])

scl_pos = 1
scl_vel = 1
scl_u = 1
scl_sig = 1
scl_z = 0.1

ang_vel = [0,0,0]
acc_cmd = np.zeros(3)

NR_epoch = 100
mempool = cp.get_default_memory_pool()

func_gpu = ker_main_(n, NR_epoch)
optimizer = gpu_optimizer(x_0, n, dt, 5, init_cond, g, ang_vel, 1000, func_gpu)
optimizer.next_opt(x_0, n, init_cond)
optimizer.scaling((scl_pos, scl_vel, scl_u, scl_sig, scl_z))

optimizer.make_mtrx()
optimizer.init_gpu()
optimizer.admm_main()
acc_cmd = cp.asnumpy(optimizer.acc_cmd_gpu)[:,np.newaxis]

optimizer.epoch = 1000

streams = [cp.cuda.Stream() for i in range(30)]

for i_stream in streams:

    with i_stream:

        t1 = time.time()
        optimizer.next_opt(x_0, n, init_cond)
        optimizer.scaling((scl_pos, scl_vel, scl_u, scl_sig, scl_z))

        optimizer.make_mtrx()
        optimizer.init_gpu()
        optimizer.admm_main()
    
        acc_cmd = cp.asnumpy(optimizer.acc_cmd_gpu)[:,np.newaxis]
        i_stream.synchronize()
        t2 = time.time()
    
        acc_cmd[:3,:] = optimizer.scale['u']@acc_cmd[:3,:]
        acc_cmd[-1,:] = optimizer.scale['sig']*acc_cmd[-1,:]
    
        print(t2 - t1, n)
        x_0 = optimizer.A@x_0 + optimizer.B@(acc_cmd[:3,:] + g[:,np.newaxis])
        init_cond['m_0'] = np.exp(np.log(init_cond['m_0']) - init_cond['alpha']*dt*acc_cmd[-1,0])

        n = n-1
    

optimizer.epoch = 0
optimizer.admm_main()

mempool.free_all_blocks()
plot(optimizer)


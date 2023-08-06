import numpy as np
import numpy.linalg as lg
import cupy as cp
from SPCEj9bbotw.kernels import *
from SPCEj9bbotw.optimizer import *
import time
import matplotlib.pyplot as plt


x_0 =np.array([2400, 450, -330, -10, -40, 10])[:,np.newaxis]
x_des = np.zeros(6)
n = 100
dt = 0.4696
init_cond = {'m_0': 2000, 'm_f': 300, 'rho1': 0.2*24000, 'rho2': 0.8*24000, 'T_max': 24000, 'alpha': 5e-4, 
            'theta': np.deg2rad(90)}
g = [-3.71, 0, 0]
# ang_vel = [2.53e-5, 0, 6.62e-5]
ang_vel = [0,0,0]
acc_cmd = np.zeros(3)
mempool = cp.get_default_memory_pool()
# pinned_mempool = cp.get_default_pinned_memory_pool()

stream = cp.cuda.Stream()
func_gpu = ker_main_(n)

optimizer = gpu_optimizer(x_0, n, dt, 5, init_cond, g, ang_vel, 2000, func_gpu)
        
        # start_event = cp.cuda.Event()

# start_event.record(stream=stream)
t1 = time.time()
optimizer.make_mtrx()
optimizer.init_gpu()

optimizer.admm_main()

y = cp.asnumpy(optimizer.y_gpu)
u = optimizer.scale['u']@(y.reshape(-1,11)[:,:3]).T
norm_u = lg.norm(u, axis=0)
plt.plot(norm_u)
plt.show()

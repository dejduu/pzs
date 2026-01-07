import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt

def Kernel(alpha, tvec, a):
    h_t = alpha*np.exp(-a*tvec)
    return np.array(h_t)

n_length = 100

tvec = np.linspace(0,2, n_length, endpoint=True)

h_t = Kernel(1.0,tvec,2.0)

x_t = sp.signal.square(2*np.pi*0.5*tvec)

x_t = np.where(tvec >= 1.0,0,x_t)

plt.plot(tvec,h_t,label="h_t")
plt.plot(tvec,x_t,label="x_t")


Conv = np.convolve(x_t,h_t,mode="full")

Conv = Conv/np.max(Conv)

t_Conv = np.linspace(0,4, np.max(Conv.shape))

plt.plot(t_Conv, Conv, label="Convolution")
plt.xlabel("t", fontsize=20)
plt.ylabel("signals", fontsize=20)
plt.legend(loc="upper right")
plt.show()
plt.savefig('convolution.png')


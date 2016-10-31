# coding: utf-8

from numpy import *
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)

# initial parameters
n_iter = 50
sz = (n_iter,)    # size of array
x = -0.37727    # truth value
z = random.normal(x, 0.1, size=sz)    # observations (normal about x, sigma=0.1)

Q = 1e-5    # process variance

# allocate space for arrays
xhat = zeros(sz)    # a posteri estimate of x
P = zeros(sz)    # a posteri error estimate
xhatminus = zeros(sz)    # a priori estimate
Pminus = zeros(sz)    # a priori error estimate
K = zeros(sz)    # gain or blending factor

R = 0.1**2    # estimate of measurement variance, change to see effect

# initial guesses
xhat[0] = 0.0
P[0] = 1.0

for k in range(1, n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1] + Q
    
    # measurement update
    K[k] = Pminus[k]/(Pminus[k] + R)
    xhat[k] = xhatminus[k] + K[k] * (z[k]-xhatminus[k])
    P[k] = (1-K[k]) * Pminus[k]

plt.figure()
plt.plot(z, 'k+', label='noisy measurement')
plt.plot(xhat, 'b-', label='a posteri estimate')
plt.axhline(x, color='g', label='truth value')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Voltage')

plt.figure()
valid_iter = range(1, n_iter)    # Pminus not valid at step 0
plt.plot(valid_iter, Pminus[valid_iter], label='a priori error estimate')
plt.title('Estimate $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('$(Voltage)^2$')
plt.setp(plt.gca(), 'ylim', [0,0.01])
plt.show()
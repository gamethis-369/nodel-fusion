import numpy as np

data = np.loadtxt('efda_100_shots.csv', delimiter=',', skiprows=1)
q = data[:,1]; p = data[:,2]
k = np.mean(p[:70] * q[:70])
pred = k / q[70:]
rmse_nodel = np.sqrt(np.mean((pred - p[70:])**2))
rmse_baseline = np.sqrt(np.mean((np.mean(p[70:]) - p[70:])**2))
print(f"k = {k:.2f}")
print(f"Nodel RMSE: {rmse_nodel:.2f} ms")
print(f"Baseline RMSE: {rmse_baseline:.2f} ms")
print(f"Lift: {rmse_baseline/rmse_nodel:.2f}x")

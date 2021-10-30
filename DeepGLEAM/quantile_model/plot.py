import numpy as np
import matplotlib.pyplot as plt

# load prediction data
data = np.load("./plotweek34result/seed34epo0.npz")

# get y_true and confidence interval
y = data['truth'].flatten()
lower_pred = data["prediction"][0, 0, :, 0]
mean_pred = data["prediction"][0, 0, :, 1]
upper_pred = data["prediction"][0, 0, :, 2]

# plot the results
plt.plot(y)
plt.plot(mean_pred)
plt.fill_between(np.arange(len(y)), lower_pred, upper_pred, color='green', alpha=.3)


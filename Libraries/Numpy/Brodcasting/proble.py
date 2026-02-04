import numpy as np

prices = np.array([100, 200, 300])
discount = 0.1
final_prices = prices - (prices * discount)
print(final_prices)
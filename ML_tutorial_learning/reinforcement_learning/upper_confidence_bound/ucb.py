import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt, log

# Importing the dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# Implementing UCB
N = dataset.shape[0]
d = dataset.shape[1]
ads_selected = []
numbers_of_selection = [1] * d
sums_of_rewards = [0] * d
total_reward = 0

for n in range(N):
    ad = 0
    max_upper_bound = 0
    for i in range(d):
        average_reward = sums_of_rewards[i] / numbers_of_selection[i]
        delta_i = sqrt(3 / 2 * (log(n + 1) / numbers_of_selection[i]))
        upper_bound = average_reward + delta_i

        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i

    ads_selected.append(ad)
    numbers_of_selection[ad] += 1
    reward = dataset.iloc[n, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward

# Visualising the results
plt.hist(ads_selected)
plt.title("Histogram of ads selections")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad was selected")
plt.show()

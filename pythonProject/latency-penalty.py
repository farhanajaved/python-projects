import matplotlib.pyplot as plt
import numpy as np

# Assuming these are your user ranges
users = np.array([2, 10, 20, 30, 40, 50])

# Random latency values for traditional and hybrid models (in milliseconds)
latency_traditional = np.array([10, 20, 30, 40, 50, 60])
latency_hybrid = np.array([8, 16, 28, 36, 44, 56])

# Random gas costs for traditional and hybrid models (in Gwei)
gas_traditional = np.array([21, 20, 22, 23, 25, 24])
gas_hybrid = np.array([15, 16, 18, 17, 19, 20])

fig, ax1 = plt.subplots(figsize=(10, 6))  # Increase figure size

# Bar plot for latency
bar_width = 0.2
index = np.arange(len(users))
bar1 = ax1.bar(index, latency_traditional, bar_width, label='Traditional Latency (ms)', color='#00008B')
bar2 = ax1.bar(index + bar_width, latency_hybrid, bar_width, label='Hybrid Latency (ms)', color='#8B0000')

ax1.set_xlabel('Number of Users')
ax1.set_ylabel('Latency (ms)')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(users)
ax1.legend(loc='upper left')

# Make the second y-axis for the gas costs
ax2 = ax1.twinx()
ax2.set_ylabel('Gas Cost (Gwei)')

# Add gas costs as line plots
line1 = ax2.plot(index + bar_width / 2, gas_traditional, label='Traditional Gas Cost (Gwei)', marker='o', color='#00008B', linestyle='--')
line2 = ax2.plot(index + bar_width / 2, gas_hybrid, label='Hybrid Gas Cost (Gwei)', marker='x', color='#8B0000', linestyle='--')
ax2.legend(loc='upper left', bbox_to_anchor=(0.001, 0.9))
ax2.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))


plt.title('Comparison of Latency and Gas Costs')
plt.tight_layout()  # Adjust the layout so everything fits
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis objects
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Data for Time Complexity vs. Gas Consumption
num_users = np.linspace(1, 50, 50)
traditional_time = np.log2(num_users)
hybrid_time = 0.5 * np.log2(num_users)
gas_traditional_time = np.full(shape=len(num_users), fill_value=21000)
gas_hybrid_time = np.full(shape=len(num_users), fill_value=100000)

# Plot Time Complexity and Gas Consumption on the first subplot
ax1 = axs[0]
ax1.set_xlabel('Number of Users')
ax1.set_ylabel('Time to Process (s)', color='tab:blue')
ax1.plot(num_users, traditional_time, 'o-', label='Traditional Time', color='tab:blue')
ax1.plot(num_users, hybrid_time, 'x--', label='Hybrid Time', color='tab:orange')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')

ax1b = ax1.twinx()
ax1b.set_ylabel('Gas Consumption', color='tab:green')
ax1b.plot(num_users, gas_traditional_time, 's-', label='Traditional Gas', linestyle='--', color='tab:blue')
ax1b.plot(num_users, gas_hybrid_time, 'D:', label='Hybrid Gas', linestyle='--', color='tab:orange')
ax1b.tick_params(axis='y', labelcolor='tab:green')
ax1b.legend(loc='upper right')

# Data for Penalty Accumulation vs. Gas Consumption
breaches = np.linspace(1, 100, 100)
traditional_penalty = breaches ** 2
hybrid_penalty = breaches ** 1.5
gas_traditional_penalty = np.full(shape=len(breaches), fill_value=21000)
gas_hybrid_penalty = np.full(shape=len(breaches), fill_value=100000)

# Plot Penalty Accumulation and Gas Consumption on the second subplot
ax2 = axs[1]
ax2.set_xlabel('Number of Breaches')
ax2.set_ylabel('Penalty Points', color='tab:blue')
ax2.plot(breaches, traditional_penalty, 'o-', label='Traditional Penalty', color='tab:blue')
ax2.plot(breaches, hybrid_penalty, 'x--', label='Hybrid Penalty', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.legend(loc='upper left')

ax2b = ax2.twinx()
ax2b.set_ylabel('Gas Consumption', color='tab:green')
ax2b.plot(breaches, gas_traditional_penalty, 's-', label='Traditional Gas', linestyle='--', color='tab:blue')
ax2b.plot(breaches, gas_hybrid_penalty, 'D:', label='Hybrid Gas', linestyle='--', color='tab:orange')
ax2b.tick_params(axis='y', labelcolor='tab:green')
ax2b.legend(loc='upper right')

plt.tight_layout()
plt.show()

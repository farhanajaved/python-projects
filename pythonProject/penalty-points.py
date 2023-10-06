import matplotlib.pyplot as plt
import numpy as np

# === CONTEXT ===
# This graph aims to compare the performance of a traditional penalty model with a hybrid penalty model
# in a blockchain context. Specifically, we look at how penalties and associated gas costs scale with an
# increasing number of SLA breaches. This gives an insight into the financial implications of using either model.

# === DATA GENERATION ===
# Number of breaches (x-axis)
breaches = np.array(range(10, 101, 10))

# Traditional model penalty in USD (for demonstration)
penalty_traditional = breaches * 0.1

# Quadratic model penalty (PQ)
penalty_quadratic = np.square(breaches + 1)

# History-based model penalty (PH)
penalty_history = penalty_quadratic * (100 - breaches) / 100

# Hybrid model penalty (P_final) = w1 * PQ + w2 * PH
w1, w2 = 0.5, 0.5
penalty_hybrid = w1 * penalty_quadratic + w2 * penalty_history

# Random gas costs for traditional and hybrid models (in Gwei, for demonstration)
gas_traditional = np.array([21, 20, 22, 23, 25, 24, 26, 27, 28, 29])
gas_hybrid = np.array([25, 26, 28, 27, 29, 30, 31, 32, 33, 34])  # Higher gas costs for the hybrid model

# === PLOT SETTINGS ===
fig, ax1 = plt.subplots(figsize=(10, 6))

# Add simple grids for better readability
ax1.grid(True)
#ax1.set_axisbelow(True)  # Puts grid below the bar plots

# === CLARITY ===
bar_width = 0.2
index = np.arange(len(breaches))

# Updated colors for academic context: dark blue and dark red
ax1.bar(index, penalty_traditional, bar_width, label='Traditional Penalty (USD)', color='#00008B')
ax1.bar(index + bar_width, penalty_hybrid, bar_width, label='Hybrid Penalty (USD)', color='#8B0000')

ax1.set_xlabel('Number of Breaches')
ax1.set_ylabel('Penalty (USD)')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(breaches)
ax1.legend(loc='upper left')

# === SCALE ===
ax2 = ax1.twinx()
ax2.set_ylabel('Gas Cost (Gwei)')

# Add simple grid for the second y-axis
#ax2.grid(True)
#ax2.set_axisbelow(True)  # Puts grid below the line plots


# Updated line colors: dashed dark blue and dashed dark red lines
line1 = ax2.plot(index + bar_width / 2, gas_traditional, label='Traditional Gas Cost (Gwei)', marker='o', color='#00008B', linestyle='--')
line2 = ax2.plot(index + bar_width / 2, gas_hybrid, label='Hybrid Gas Cost (Gwei)', marker='x', color='#8B0000', linestyle='--')
ax2.legend(loc='upper left', bbox_to_anchor=(0.001, 0.9))
ax2.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

plt.title('Comparison of Penalties and Gas Costs')
plt.tight_layout()
plt.show()

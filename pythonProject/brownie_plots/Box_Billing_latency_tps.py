import matplotlib.pyplot as plt
import numpy as np

# Your data for different numbers of users
num_users = np.array(range(2, 50))  # 2 to 50 users
avg_latency = np.array([
    0.0153, 0.0115, 0.0099, 0.0105, 0.0096, 0.0100, 0.0104, 0.0112, 0.0113,
    0.0103, 0.0096, 0.0095, 0.0098, 0.0106, 0.0108, 0.0106, 0.0107, 0.0106,
    0.0109, 0.0107, 0.0108, 0.0105, 0.0101, 0.0103, 0.0105, 0.0104, 0.0103,
    0.0098, 0.0104, 0.0104, 0.0100, 0.0099, 0.0097, 0.0098, 0.0097, 0.0099,
    0.0100, 0.0100, 0.0102, 0.0101, 0.0100, 0.0098, 0.0097, 0.0097, 0.0101,
    0.0101, 0.0097, 0.0094, 0.0094
])

# Create a new figure
fig, ax = plt.subplots()

# Create a violin plot for Average Latency
ax.violinplot(avg_latency, positions=num_users, vert=True, showmeans=True, showmedians=True)

# Label the Y-axis
ax.set_ylabel('Average Latency (s)')

# Label the X-axis
ax.set_xlabel('Number of Users')
ax.set_xticks(num_users[::5])  # set the tick locations to every 5th point for clarity
ax.set_xticklabels(num_users[::5])  # set the tick labels

# Add a title
ax.set_title('Violin Plot of Average Latency for Different Numbers of Users')

# Show the plot
plt.show()
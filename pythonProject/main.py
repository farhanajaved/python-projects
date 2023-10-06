import matplotlib
matplotlib.use('TkAgg')  # This sets the backend to TkAgg
import matplotlib.pyplot as plt
import time

class SmartContract:
    PENALTY_FEE = 100  # Assume a fixed penalty fee for simplicity

    @staticmethod
    def calculate_penalty(breaches):
        # Simulated logic for calculating penalty for SLA breaches
        total_penalty = 0
        for breach in breaches:
            total_penalty += SmartContract.PENALTY_FEE
        return total_penalty

# Measure execution times for varying number of breaches
breaches_list = list(range(1, 51))  # From 1 breach to 50 breaches
times = []

for breaches in breaches_list:
    start_time = time.time()
    SmartContract.calculate_penalty([1] * breaches)  # Simulate 'breaches' number of breaches
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(breaches_list, times, marker='o', linestyle='-', color='b')
plt.title("Execution Time vs. Number of Breaches")
plt.xlabel("Number of Breaches")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.savefig('plot.png')
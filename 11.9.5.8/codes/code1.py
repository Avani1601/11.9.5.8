import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n)
def y(n):
    return 3*n**2 + 13*n + 10

# Define the range of n
n_values = np.arange(0, 11)

# Compute y(n) for each value of n
y_values = y(n_values)

# Read data from the file
data_file = "data1.dat"
with open(data_file, "r") as file:
    lines = file.readlines()

# Extract data
n_values_data = []
y_values_data = []
highlight_index = None
for line in lines[1:]:
    parts = line.split()
    n = int(parts[0])
    y_val = int(parts[1])
    n_values_data.append(n)
    y_values_data.append(y_val)

    # Check for highlight index line
    if len(parts) == 4 and parts[2] == "index:":
        highlight_index = int(parts[3])

# Plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt=' ', label="y(n)")

# Highlight point at n=9 with red color
plt.stem(9, y(9), linefmt='r-', markerfmt='ro', basefmt='r-')

# Highlight point from data file
if highlight_index is not None:
    plt.stem(n_values_data[highlight_index], y_values_data[highlight_index], linefmt='g-', markerfmt='go', basefmt='g-')

plt.xlabel("n")
plt.ylabel("y(n)")

plt.legend()
plt.grid(True)

# Set x-axis ticks to display all values of n
plt.xticks(np.arange(0, max(max(n_values), max(n_values_data))+1, 1))

# Save the plot as PNG image
plt.savefig("combined_plot.png")

# Show the plot
plt.show()


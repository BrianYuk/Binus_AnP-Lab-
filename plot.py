import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Line plot
plt.plot(x, y, color='#ff6347', linestyle='--', linewidth=2, marker='o')

plt.title("Line Plot of Prime Numbers")

# Axes label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add grid lines
plt.grid(True)

# Add a legend
plt.legend()

# Find the maximum y-value and its corresponding x-value
max_y = max(y)
max_x = x[y.index(max_y)]

# Annotate the maximum y-value
plt.annotate(f'Max Value: {max_y}', xy=(max_x, max_y), xytext=(max_x+0.5, max_y+1),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Save the plot as a PNG file
plt.savefig('plot.png')

plt.show()

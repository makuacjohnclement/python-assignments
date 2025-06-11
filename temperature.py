import matplotlib.pyplot as plt

# %matplotlib inline   this line is not needed in a script, it's used in Jupyter notebooks

# This script creates a line plot of temperature readings over a week using matplotlib

# Temperature data for the week
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linewidth=2, markersize=8, color='blue')

# Customize the plot
plt.title('Temperature Readings Over a Week', fontsize=16, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)

# Add value labels on each point
for i, temp in enumerate(temperatures):
    plt.annotate(f'{temp}°C', (i, temp), textcoords="offset points", 
                xytext=(0,10), ha='center', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

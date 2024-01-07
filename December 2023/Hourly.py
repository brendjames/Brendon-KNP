import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("E:/BJ/KNP/Brendon-KNP/December 2023/cleaned_data_dec2023.csv")

# Convert the "Time" column to datetime
data["Time"] = pd.to_datetime(data["Time"], errors='coerce')

# Group the data by hour and count the occurrences
hourly_counts = data.groupby(data["Time"].dt.hour).size()

# Plot the data on a bar graph
hourly_counts.plot(kind="bar")

# Set the labels and title
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Hourly Breakdown")

# Save the graph as "hourly.jpg"
plt.savefig("hourly.jpg")

# Show the graph
plt.show()
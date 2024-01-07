import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv("E:\BJ\KNP\Brendon-KNP\December 2023\Data\Data Findings\cleaned_data_dec2023.csv")

# Define the keywords to look for
keywords = ["Leopard", "Leopards"]

# Filter the DataFrame to include only rows where the "Animal Type and Number" column contains any of the keywords
filtered_data = data[data["Animal Type and Number"].str.contains('|'.join(keywords), na=False)]

# Save the filtered DataFrame to a new CSV file
filtered_data.to_csv("E:\BJ\KNP\Brendon-KNP\December 2023\Data\Data Findings\Leopards.csv", index=False)
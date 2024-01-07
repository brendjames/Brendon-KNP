import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv("E:\BJ\KNP\Brendon-KNP\December 2023\Data\Data Findings\cleaned_data_dec2023.csv")

# Define the keywords to look for
keywords = ["Safari", "Safaris", "Tours"]

# Filter the DataFrame to include only rows where the "Tinged By" column contains any of the keywords
filtered_data = data[data["Tinged By"].str.contains('|'.join(keywords), na=False)]

# Print the count
print(f"The number of rows containing the keywords is: {len(filtered_data)}")

# Save the filtered DataFrame to a new CSV file
filtered_data.to_csv("E:\BJ\KNP\Brendon-KNP\December 2023\Green Mambas.csv", index=False)
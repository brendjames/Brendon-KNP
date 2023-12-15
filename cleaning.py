import pandas as pd

# Read the CSV files
df1 = pd.read_csv('Dec15.csv')
df2 = pd.read_csv('Dec13.csv')

# Concatenate the dataframes
merged_df = pd.concat([df1, df2])

# Print the column names
print(merged_df.columns)

# Drop duplicate rows
merged_df = merged_df.drop_duplicates()

# Perform data cleaning operations here
columns_to_drop = ['tweet_date', 'ID']
merged_df = merged_df.drop(columns=[col for col in columns_to_drop if col in merged_df.columns])

# Save the cleaned data to a new CSV file
merged_df.to_csv('cleaned_data.csv', index=False)
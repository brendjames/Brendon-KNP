import os
import pandas as pd

folder_path = 'e://BJ//KNP//Brendon-KNP//December 2023'
cleaned_files = []

# List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# For each CSV file in the specified folder
for file in csv_files:
    # Construct the full file path by joining the folder path and the file name
    file_path = os.path.join(folder_path, file)
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    # Drop the 'Tweet Date' and 'ID' columns from the DataFrame
    df.drop(columns=['Tweet Date', 'ID'], inplace=True)
    # Construct the full path for the cleaned CSV file
    cleaned_file = os.path.join(folder_path, f'{file.split(".")[0]}_cleaned.csv')
    # Write the cleaned DataFrame to a new CSV file
    df.to_csv(cleaned_file, index=False)
    # Add the cleaned file to the list of cleaned files
    cleaned_files.append(cleaned_file)

# Merging all cleaned CSVs into a single DataFrame
dfs = [pd.read_csv(file) for file in cleaned_files]
merged_df = pd.concat(dfs, ignore_index=True)
merged_df.drop_duplicates(inplace=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(os.path.join(folder_path, 'cleaned_data_dec2023.csv'), index=False)

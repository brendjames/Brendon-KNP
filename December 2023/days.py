import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned CSV file into a DataFrame
df = pd.read_csv('E:\BJ\KNP\Brendon-KNP\December 2023\cleaned_data_dec2023.csv')

# Parse the 'Title' column as datetime
df['Title'] = pd.to_datetime(df['Title'], format='%b %d, %Y · %I:%M %p %Z', errors='coerce')

# Extract the day of the month from each date
df['Day'] = df['Title'].dt.day

# Count the number of tweets for each day
tweet_counts = df['Day'].value_counts().sort_index()

# Create a bar graph of the tweet counts
plt.figure(figsize=(10, 6))
plt.bar(tweet_counts.index, tweet_counts.values)
plt.xlabel('Day of the Month')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets per Day')
plt.show()
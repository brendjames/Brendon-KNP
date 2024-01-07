import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned CSV file into a DataFrame
df = pd.read_csv('E:\BJ\KNP\Brendon-KNP\December 2023\cleaned_data_dec2023.csv')

# Parse the 'Title' column as datetime
df['Title'] = pd.to_datetime(df['Title'], format='%b %d, %Y · %I:%M %p %Z', errors='coerce')

# Extract the hour from each date
df['Hour'] = df['Title'].dt.hour

# Count the number of tweets before and after 12:00
tweets_before_12 = df[df['Hour'] < 12].shape[0]
tweets_after_12 = df[df['Hour'] >= 12].shape[0]

# Create a bar graph of the tweet counts
bars = plt.bar(['Before 12:00', 'After 12:00'], [tweets_before_12, tweets_after_12], color=['blue', 'orange'])

# Add the total number of tweets on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50, yval, ha='center', va='bottom')

plt.xlabel('Time of Day')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets Before and After 12:00')
plt.show()
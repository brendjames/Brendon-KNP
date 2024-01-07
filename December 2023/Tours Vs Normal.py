import pandas as pd
import matplotlib.pyplot as plt

# Read the Green Mambas.csv file
green_mambas_df = pd.read_csv("E:\BJ\KNP\Brendon-KNP\December 2023\Green Mambas.csv")

# Read the cleaned_data_dec2023.csv file
cleaned_data_df = pd.read_csv("E:\BJ\KNP\Brendon-KNP\December 2023\cleaned_data_dec2023.csv")

# Get the number of tweets in each file
green_mambas_tweets = len(green_mambas_df)
cleaned_data_tweets = len(cleaned_data_df)

# Calculate the difference in tweet counts
difference = cleaned_data_tweets - green_mambas_tweets

# Create a bar graph
labels = ["Green Mambas", "Cleaned Data"]
tweet_counts = [green_mambas_tweets, cleaned_data_tweets]

plt.bar(labels, tweet_counts)
plt.xlabel("File")
plt.ylabel("Number of Tweets")
plt.title("Comparison of Tweet Counts")
plt.show()

# Print the difference in tweet counts
print(f"The difference in tweet counts is: {difference}")

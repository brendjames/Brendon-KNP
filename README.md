# NO LONGER WORKING DUE TO NITTER BEING TAKEN OFFLINE


# Nitter(Twitter) Scraper

This Python script is designed to scrape tweets from a specific Twitter-like platform (Nitter) and extract specific information from those tweets. The primary goal is to extract data for local storage and subsequent data analysis.

# Overview
The script utilizes Selenium and BeautifulSoup to automate web browsing and extract tweet information from a given Nitter user's timeline. Extracted data includes various attributes of each tweet, such as ID, time, animal type and number, location, rating, tinger, title, and tweet date.


## Requirements

- Python 3.x
- Selenium
- Beautiful Soup 4
- Chrome WebDriver

## Installation

1. Install Python (if not already installed): [Python Installation Guide](https://www.python.org/downloads/)
2. Install required packages:
   bash
   pip install selenium beautifulsoup4
   
3. Download Chrome WebDriver: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
4. Ensure the Chrome WebDriver is in your system PATH.

## Usage

1. Clone the repository or download the script.
2. Ensure all dependencies are installed as mentioned in the Requirements section.
3. Run the script:
   bash
   python 15.py
   
## Configuration

- Modify the script to change the target Twitter profile (`driver.get('https://nitter.net/LatestKruger')`) or adjust the scraping parameters.
- Customize the CSV output file name (`'xxx.csv'`) as needed.

## Data Analysis

Once the data is locally stored, it can be utilized for various analytics purposes.
- Examples of analytics might include:
   - Sentiment Analysis: Analyzing the sentiment of tweets based on their content or ratings.
   - Location-based Analysis: Understanding trends or occurrences based on the locations mentioned in tweets.
   - Engagement Metrics: Calculating engagement rates or trends based on tinger data.
   - Time-based Analysis: Studying tweet frequency or popularity trends over time.
   - Correlation Studies: Exploring relationships between attributes like ratings and animal type/numbers.

## Notes

- The script fetches +-100 tweets from the target profile.
- The script includes error handling for potential issues during scraping.
- Ensure compliance with the platform's terms of service and rate limits when scraping.
- The extracted data can be further cleaned, processed, and analyzed using various data analysis libraries in Python such as Pandas, Matplotlib, or Natural Language Toolkit (NLTK), among others

## Disclaimer

This script is provided as-is and may require updates based on changes to the website structure or Twitter's policies.

---


# Nitter0(Twitter) Scraper

This Python script enables scraping tweets from a specific Twitter profile using Selenium and Beautiful Soup. The script navigates through the profile page, collects tweet details, and stores them in a CSV file.

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

## Notes

- The script fetches 100 tweets from the target profile.
- It extracts tweet details such as ID, time, animal type and number, location, rating, tinged by, title, and tweet date.
- The extracted data is saved in a CSV file named `xxx.csv`.

## Disclaimer

This script is provided as-is and may require updates based on changes to the website structure or Twitter's policies.

---

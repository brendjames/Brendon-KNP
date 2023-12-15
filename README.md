# Twitter Web Scraper

This repository contains a Python script for scraping tweets from a Nitter(Twitter) account using Selenium and BeautifulSoup.

## Description

The script navigates to a specified Nitter account using Selenium, then scrapes the tweets on the page using BeautifulSoup. It scrolls down the page to load more tweets, and repeats this process a specified number of times. The scraped tweets are written to a CSV file.

The script extracts the following information from each tweet:

- ID
- Time
- Animal Type and Number
- Location
- Rating
- Tinged By
- Title
- Tweet Date

## Requirements

- Python 3
- Selenium
- BeautifulSoup
- Chrome WebDriver


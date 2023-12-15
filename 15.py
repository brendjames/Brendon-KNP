import csv
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_tweets():
    # Setup the WebDriver
    driver = webdriver.Chrome()

    # Navigate to the page
    driver.get('https://nitter.net/LatestKruger')

    # Wait for the page to load
    time.sleep(10)  # Not ideal, consider using WebDriverWait

    # Open the CSV file to write data
    with open('Dec15.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        # Write headers to the CSV file
        csv_writer.writerow(['ID', 'Time', 'Animal Type and Number', 'Location', 'Rating', 'Tinged By', 'Title', 'Tweet Date'])
        
        # Define the ID outside the page processing loop    
        i = 1

        for _ in range(100):  # Repeat the process 10 times
            # Scroll down until new content stops loading or a certain condition is met
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)  # Adjust this value based on the page loading speed

                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # Get the updated HTML content after loading more tweets
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # Find all tweet content divs
            tweet_content_divs = soup.find_all('div', class_='tweet-content media-body')

            for i, tweet_content_div in enumerate(tweet_content_divs, start=1):
                if tweet_content_div is not None:
                    # Extracting different parts of the tweet
                    tweet_content = tweet_content_div.get_text(strip=True)
                    lines = tweet_content.split('\n')
                    lines += [''] * (6 - len(lines))
                    tweet_time = lines[0]
                    animal_type_and_number = lines[1]
                    rating = lines[-2]
                    match = re.search(r'\d/5', rating)
                    if match:
                        rating = match.group()
                    else:
                        continue
                    tinger = lines[-1]
                    tinger = tinger.split('Tinged by ')[-1]
                    location = ' '.join(lines[2:-2])

                    # Extracting tweet date for each tweet content div
                    tweet_div = tweet_content_div.parent
                    tweet_date_span = tweet_div.find('span', class_='tweet-date')
                    title = ""
                    tweet_date = ""
                    if tweet_date_span:
                        tweet_date_a = tweet_date_span.find('a')
                        if tweet_date_a:
                            title = tweet_date_a.get('title')
                            tweet_date = tweet_date_a.text  # Extracting the tweet date text

                    # Write extracted data to CSV
                    csv_writer.writerow([i, tweet_time, animal_type_and_number, location, rating, tinger, title, tweet_date])

            # Finding a 'Next' button and clicking it
            try:
                next_page_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Load more')))
                next_page_link.click()
                time.sleep(5)  # Wait for the new content to load
            except Exception as e:
                print("No more 'Load more' button found.")
                break

            # Wait for the appearance of elements related to newly loaded content
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "tweet-content")))

    driver.quit()  # Close the WebDriver once done

if __name__ == "__main__":
    scrape_tweets()
import csv
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_tweets():
    driver = webdriver.Chrome()
    driver.get('https://nitter.net/LatestKruger')
    time.sleep(10)

    with open('Dec15v1.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['ID', 'Time', 'Animal Type and Number', 'Location', 'Rating', 'Tinged By', 'Title', 'Tweet Date'])

        i = 1  # Define 'i' outside the loop for row numbering

        for _ in range(100):  # Repeat the process 100 times
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tweet_content_divs = soup.find_all('div', class_='tweet-content media-body')

            for row_number, tweet_content_div in enumerate(tweet_content_divs, start=i):
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

                    # Filtering locations starting with 'H' or 'S'
                    if not (location.startswith('H') or location.startswith('S')):
                        continue  # Skip if location doesn't start with 'H' or 'S'

                    tweet_div = tweet_content_div.parent
                    tweet_date_span = tweet_div.find('span', class_='tweet-date')
                    title = ""
                    tweet_date = ""
                    if tweet_date_span:
                        tweet_date_a = tweet_date_span.find('a')
                        if tweet_date_a:
                            title = tweet_date_a.get('title')
                            tweet_date = tweet_date_a.text

                    csv_writer.writerow([row_number, tweet_time, animal_type_and_number, location, rating, tinger, title, tweet_date])

            try:
                next_page_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Load more')))
                next_page_link.click()
                time.sleep(5)
            except Exception as e:
                print("No more 'Load more' button found.")
                break

            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "tweet-content")))

            i = row_number + 1  # Update 'i' to the next row number for the next iteration

    driver.quit()

if __name__ == "__main__":
    scrape_tweets()

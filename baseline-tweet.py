from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time
import re

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def load_page(driver, urlpage):
    try:
        driver.get(urlpage)
        time.sleep(5)  # wait for the page to load

        # Find the "Load more" button and get its 'href' attribute
        load_more_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".show-more a")))
        href = load_more_button.get_attribute('href')

        return href
    except Exception as e:
        print(f"Error loading page: {e}")
        driver.quit()
        return None

def main():
    url = 'https://nitter.net/LatestKruger'
    driver = setup_driver()
    load_page(driver, url)

    time.sleep(0.5)  # wait for the page to load

    for _ in range(10):
        href = load_page(driver, url)
        if href is not None:
            url = 'https://nitter.net/LatestKruger' + href
        else:
            break
        time.sleep(5)  # wait for the page to load

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tweet_content_divs = soup.find_all('div', class_='tweet-content media-body')
    with open('tweet11.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['ID', 'Time', 'Animal Type and Number', 'Location', 'Rating', 'Tinged By'])  # write headers
        for i, tweet_content_div in enumerate(tweet_content_divs, start=1):
            if tweet_content_div is not None:
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
                csv_writer.writerow([i, tweet_time, animal_type_and_number, location, rating, tinger])

    driver.quit()

if __name__ == "__main__":
    main()
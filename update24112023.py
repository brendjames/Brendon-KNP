from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv


# Initialize the Chrome driver
driver = webdriver.Chrome()

# Go to the webpage
driver = webdriver.Chrome(executable_path=r'"C:\Users\btran\.wdm\drivers\chromedriver\win32\119.0.6045.105\chromedriver.exe"')

# Wait for the sightings list to load
wait = WebDriverWait(driver, 10)
sightings_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sightings-list")))

# Parse the page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the Sightings List
sightings_list = soup.find('div', {'class': 'sightings-list'})

# Extract the sightings
sightings = sightings_list.find_all('div', {'class': 'sighting'})

# Prepare the CSV file
with open('sightings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["animal", "location", "date", "time"])

    # Loop through the sightings and write them to the CSV file
    for sighting in sightings:
        animal = sighting.find('div', {'class': 'animal'}).text
        location = sighting.find('div', {'class': 'location'}).text
        date = sighting.find('div', {'class': 'date'}).text
        time = sighting.find('div', {'class': 'time'}).text

        writer.writerow([animal, location, date, time])

# Close the browser
driver.quit()

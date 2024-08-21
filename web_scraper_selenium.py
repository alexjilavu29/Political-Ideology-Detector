import csv
import os
import time
import random
import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Ensure the directory exists
os.makedirs('data', exist_ok=True)

urls = [
    'https://www.rsbnetwork.com/news/trump-celebrates-big-night-in-america-perfect-endorsement-score-in-latest-primary-wins/',
    'https://www.rsbnetwork.com/news/president-trump-to-do-major-interview-with-elon-musk/',
    'https://www.rsbnetwork.com/news/every-americans-nightmare-trump-campaign-responds-to-walz-as-vp-pick/'
]

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = uc.Chrome(service=service, options=chrome_options)

with open('data/articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text'])

    for url in urls:
        try:
            driver.get(url)
            time.sleep(3)  # Allow some time for the page to load

            print(driver.page_source)

            # Wait for the title element to be present
            title_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )

            # Wait for the article element to be present
            article_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.post-entry'))
            )

            title_element = driver.find_element(By.TAG_NAME, 'h1')
            article_element = driver.find_element(By.CSS_SELECTOR, 'div.post-entry')

            title = title_element.text if title_element else 'Title not found'
            article_text = article_element.text if article_element else 'Article text not found'

            writer.writerow([title, article_text])

        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")
            writer.writerow([f"Error with URL: {url}", "Unknown error"])

# Close the driver
driver.quit()
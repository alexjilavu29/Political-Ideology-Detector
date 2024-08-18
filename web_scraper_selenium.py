import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
driver = webdriver.Chrome(service=service, options=chrome_options)

with open('data/articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text'])

    for url in urls:
        try:
            driver.get(url)
            time.sleep(3)  # Allow some time for the page to load

            title_element = driver.find_element(By.CSS_SELECTOR, 'h1.post-title.single-post-title.entry-title')
            article_element = driver.find_element(By.CSS_SELECTOR, 'div.post-entry.blockquote-style-1')

            title = title_element.text if title_element else 'Title not found'
            article_text = article_element.text if article_element else 'Article text not found'

            writer.writerow([title, article_text])

        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")
            writer.writerow([f"Error with URL: {url}", "Unknown error"])

# Close the driver
driver.quit()
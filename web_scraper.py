import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import random

# Ensure the directory exists
os.makedirs('data', exist_ok=True)

# List of URLs to scrape
urls = [
    'https://www.rsbnetwork.com/news/trump-celebrates-big-night-in-america-perfect-endorsement-score-in-latest-primary-wins/',
    'https://www.rsbnetwork.com/news/president-trump-to-do-major-interview-with-elon-musk/',
    'https://www.rsbnetwork.com/news/every-americans-nightmare-trump-campaign-responds-to-walz-as-vp-pick/'
]

# List of User Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0',
]

session = requests.Session()

with open('data/articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Text'])

    for url in urls:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.content, 'html.parser')

            title_element = soup.find('h1', class_='post-title single-post-title entry-title')
            article_element = soup.find('div', class_='post-entry blockquote-style-1')

            if title_element:
                title = title_element.get_text()
            else:
                title = 'Title not found'

            if article_element:
                article_text = article_element.get_text()
            else:
                article_text = 'Article text not found'

            writer.writerow([title, article_text])

            # Random delay to avoid detection
            time.sleep(random.uniform(1, 3))

        except requests.exceptions.RequestException as e:
            print(f"HTTP error occurred for URL {url}: {e}")
            writer.writerow([f"Error with URL: {url}", "HTTP error"])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")
            writer.writerow([f"Error with URL: {url}", "Unknown error"])
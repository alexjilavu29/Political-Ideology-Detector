# Political Ideology Classification Project

This repository contains an ongoing project focused on building an AI model that classifies text on the political Left-Right spectrum using BERT, a transformer-based model. The code includes data preprocessing, model training, and testing, as well as web scraping tools to gather political articles. **Note:** This is a work-in-progress, and the code may not always work as expected.

## Project Overview

The main goal of this project is to create a binary classifier that identifies whether a given text leans politically left or right. The project involves four major components:

1. **BERT-based Model for Political Ideology Detection**  
   - The main script `bert_model_political.py` contains the integration of BERT to perform the classification task.
   
2. **Model Testing**  
   - The script `bert_test.py` tests the viability of BERT by experimenting with it on the IMDB dataset.

3. **Web Scrapers**  
   - Two scrapers, `web_scraper.py` and `web_scraper_selenium.py`, gather political news articles from the web to create training data for the model.

## Features

### BERT Model Integration (`bert_model_political.py`)
- Utilizes the pre-trained BERT (`bert-base-uncased`) model for classifying text as "left" or "right."
- Trains the model using a dataset of political texts.
- Supports the following:
  - Training on labeled datasets with customizable parameters.
  - Evaluation based on accuracy and classification reports.
  - Predicting the political bias of new texts.

### Testing BERT Performance (`bert_test.py`)
- Tests the performance of the BERT model on the IMDB dataset.
- Achieved a validation accuracy of 90%.
- Script includes functionality to:
  - Load and preprocess data.
  - Train and evaluate BERT's ability to classify text as "positive" or "negative" sentiment, to ensure its suitability for political classification.

### Web Scrapers for Data Collection
- **Basic Web Scraper (`web_scraper.py`)**: Gathers news articles using `requests` and `BeautifulSoup`.
- **Selenium Web Scraper (`web_scraper_selenium.py`)**: Uses Selenium for sites with dynamic content that requires JavaScript to render.
- Both scrapers store the gathered articles in CSV format for later use in model training.

## How to Run

### 1. Install Dependencies
To get started, clone the repository and install the required Python packages:
```bash
git clone https://github.com/yourusername/political-ideology-classification.git
cd political-ideology-classification
pip install -r requirements.txt
```

## 2. Train the BERT model

The `bert_model_political.py` file is the primary code that trains a BERT model to classify political ideologies as either left-leaning or right-leaning based on the input text. This script relies on a political dataset and BERT (Bidirectional Encoder Representations from Transformers) to perform the classification task.

The training process involves:

- **Text Preprocessing**: Tokenizing text data using the BERT tokenizer to prepare it for input into the model.
- **Model Definition**: Using a pre-trained BERT model (`bert-base-uncased`) and adding a custom classification head for binary classification.
- **Training and Evaluation**: The model is trained for several epochs on the provided dataset and then evaluated using metrics like accuracy and classification reports.

During training, a learning rate scheduler (`get_linear_schedule_with_warmup`) is used to adjust the learning rate, and AdamW optimizer is employed.

### Example Commands:
To train the model, simply run:
```bash
python bert_model_political.py
```

## 3. Model Testing

The `bert_test.py` script is used to validate the model's accuracy and ensure that BERT is an appropriate model for this task. It was initially tested on the IMDB sentiment dataset, achieving a 90% accuracy after training for 4 epochs on a GPU.

This test script follows a similar structure as the main model script, with the key difference being the dataset used for validation and training (IMDB reviews).

### Example Commands:
To test the model:
```bash
python bert_test.py
```

## 4. Web Scraping Data

In order to gather more training data, the project includes two web scraping scripts:

- **`web_scraper.py`**: Uses the `requests` library and BeautifulSoup to scrape political news articles from predefined URLs. The extracted data is saved in a CSV format to be used for training.
- **`web_scraper_selenium.py`**: Uses Selenium with the undetected Chrome WebDriver to scrape articles from websites that may have more complex dynamic loading content (e.g., JavaScript-heavy sites).

Both scripts store the scraped data in a file called `data/articles.csv`, with each row containing the article title and content.

### Example Commands:
To scrape data using BeautifulSoup:
```bash
python web_scraper.py
```

To scrape data using Selenium:
```bash
python web_scraper_selenium.py
```

### Notes on Web Scraping:
- Ensure that you have the necessary permissions to scrape the targeted websites.
- The scripts introduce random delays between requests to avoid detection as a bot.

## 5. Usage and Deployment

1. **Ensure Dependencies are Installed**: 
   - Install all the necessary dependencies listed in the `requirements.txt` file using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Training the Model**: 
   - After gathering the dataset, run the training script to train the BERT model on the political dataset.

3. **Model Evaluation**: 
   - Use the `bert_test.py` script to test the model on additional datasets and validate its performance.

## 6. Limitations and Future Work

- The current implementation is still an **ongoing project**, and the model may not work as intended for all text inputs, especially if the text is ambiguous or contains ideologically mixed viewpoints.
- The data used for training may need to be expanded for improved accuracy and generalization to diverse political content.
- **Planned improvements**:
   - Further fine-tuning of the model on a more diverse dataset.
   - Implementation of a web-based UI for live predictions.
   - Expanding the political spectrum beyond binary classifications (left-right).

## 7. Contributions

Contributions are welcome! Feel free to submit pull requests or open issues if you encounter any bugs or have suggestions for improvements.

## 8. License

This project is licensed under the MIT License. See the `LICENSE` file for details.
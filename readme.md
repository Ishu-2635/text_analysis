# Web Scraping and Text Analysis with Python

This project performs web scraping and text analysis using a custom-built NLP pipeline in Python. It scrapes article content from a list of URLs, performs text preprocessing, and extracts various linguistic and sentiment-based metrics.

---


## 🧰 Tools & Libraries Used

- **Python 3.9+**
- `pandas` - for data manipulation
- `BeautifulSoup` - for HTML parsing
- `requests` - to fetch HTML content
- `nltk` - tokenization and sentence splitting
- `re` - for regular expressions
- `os`, `string`, `time` - standard library utilities

---

## 🔎 What This Project Does

### 1. Web Scraping
- Reads URLs from `Input.xlsx`
- Fetches page content using `requests`
- Extracts title and article content using `BeautifulSoup`
- Cleans HTML tags, removes special characters, and writes cleaned text to `.txt` files

### 2. Text Preprocessing
- Tokenizes text into sentences and words
- Removes punctuation and stopwords
- Stores cleaned and structured tokens in dictionaries

### 3. Sentiment & Readability Analysis
Extracts the following metrics for each article:
- **Positive & Negative Scores**
- **Polarity Score** = (Positive - Negative) / (Positive + Negative + ε)
- **Subjectivity Score** = (Positive + Negative) / Total Words
- **Average Sentence Length**
- **Complex Word Count** (based on syllables)
- **Percentage of Complex Words**
- **Fog Index** (Readability score)
- **Average Word Length**

---

## 📊 Output
- Text files for each article in the `scraped100/` directory
- Metrics printed in console and in out data structure excel file

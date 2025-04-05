# Web Scraping Project – CS 325

## Overview

This project is a simple yet effective Python-based web scraper that extracts business-related headlines from a list of URLs. It uses the `requests` and `BeautifulSoup` libraries to parse and collect `<h1>`, `<h2>`, and `<h3>` headings, then saves the cleaned, de-duplicated results to a text file.

---

## Project Structure

- `input_urls.txt` – Text file containing one business-related news URL per line.
- `scraper.py` – The main Python script for scraping headings.
- `output_headings.txt` – Output file containing the final list of unique headlines.

---

## Setup Instructions

1. **Clone the repository** and check out the scraping branch:

   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   git checkout -b webScraping
   ```

2. **Install dependencies** (preferably inside a virtual environment):

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Add URLs to scrape**  
   Open `input_urls.txt` and paste one URL per line. Example:

   ```
   https://www.businessnewsdaily.com
   https://www.reuters.com/business/
   https://www.cnbc.com/business/
   ```

4. **Run the scraper:**

   ```bash
   python scraper.py
   ```

5. **Check your output:**  
   The scraped headings will be saved in `output_headings.txt`.

---

## Features

- Extracts text from `<h1>`, `<h2>`, and `<h3>` tags.
- Cleans and removes duplicate entries.
- Gracefully handles request errors and invalid URLs.
- Saves the results in sorted order for easier reading.

---

## Example Output

`output_headings.txt`:

```
Amazon Launches New Business Services
Breaking: Federal Reserve Raises Interest Rates
Market Trends for Q2 2025
The Future of Remote Work
```

---

## Error Handling

- If `input_urls.txt` is missing, the script will exit with an error message.
- Failed network requests or invalid pages will be logged to the console but won’t crash the script.
- Only non-empty headings are saved.

---

## Technologies Used

- [Python 3](https://www.python.org/)
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

---

## Notes

- Designed for educational use in **CS 325 –Software Engineering**.
- Can be extended to support CSV, JSON, or database output.
- Ideal for experimenting with HTML parsing and web automation.

---

## License

This project is for academic use only. All content scraped belongs to its respective sources. Use responsibly.

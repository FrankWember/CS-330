# Web Scraping Project – CS 325

## Overview

This project scrapes business-related headlines from multiple news websites. It uses the Python libraries `requests` and `BeautifulSoup` to extract headlines (`<h1>`, `<h2>`, `<h3>`) from provided URLs and stores the results in a text file.

---

## Input

- `input_urls.txt`: A list of business news URLs, one per line.

## Output

- `output_headings.txt`: A list of cleaned, de-duplicated headlines extracted from the URLs.

---

## Setup Instructions

1. **Clone the repo** and switch to the `webScrapping` branch:

```bash
git clone <your-repo-url>
cd <repo-name>
git checkout -b webScrapping
```

# 📰 LLM-Powered Sentiment Analyzer for Business Headlines

This project scrapes headlines from popular business and finance news websites, analyzes their sentiment using a local LLM (e.g., TinyLlama via Ollama), and saves the results to a file. The full application is containerized using Docker.

---

## 📁 Project Structure

```
Project3/
├── scraper.py               # Scrapes headings from provided URLs
├── sentiment_analyzer.py   # Analyzes headline sentiment using a local LLM
├── main.py                 # Orchestrates scraping and the sentiment analysis
├── requirements.txt        # List of Python dependencies
├── Dockerfile              # Builds the Python environment image
├── docker-compose.yml      # Orchestrates container setup
├── input_urls.txt          # List of all the URLs to scrape
├── output/
│   ├── headings.txt        # Extracted headlines
│   └── sentiments.txt      # Sentiment results
├── test_scraper.py         # Pytest for HeadingScraper
└── test_sentiment_analyzer.py  # Pytest for LLMSentimentAnalyzer
```

---

## How It Works

### Step-by-step:

1. Reads news URLs from `input_urls.txt`
2. Scrapes all `<h1>`, `<h2>`, and `<h3>` headlines from those URLs
3. Sends each headline to a local LLM (via Ollama)
4. Stores the sentiment result (Positive/Negative/Neutral) in `output/sentiments.txt`

---

## Running with Docker

> Make there is Docker and [Ollama](https://ollama.com) installed and that `ollama run tinyllama` is running locally on your machine.

### 1. Run Ollama separately on host:

```bash
ollama run tinyllama
```

### 2. Build & run app with Docker:

```bash
docker-compose up --build
```

Output files will be saved in the `output/` directory on your host machine.

---

## Running Tests

This project includes two basic tests using `pytest`.

### Run both tests:

```bash
pytest test_scraper.py
pytest test_sentiment_analyzer.py
```

### Tests included:

- ✅ `test_scraper_creates_output_file` — ensures the scraper extracts headings and writes to a file
- ✅ `test_sentiment_analyzer_writes_sentiments` — checks the sentiment analyzer produces expected output

---

## ⚙️ Environment Variables

| Variable     | Description                            | Example                                             |
| ------------ | -------------------------------------- | --------------------------------------------------- |
| `LLM_SERVER` | URL for the local LLM inference server | `http://host.docker.internal:11434` (inside Docker) |

---

## ✅ Dependencies

All dependencies are listed in `requirements.txt`:

- `requests`
- `beautifulsoup4`

Install locally with:

```bash
pip install -r requirements.txt
```

---

## ✍️ Authors & Credit

Created by Frank Wember. LLM-based inference via [Ollama](https://ollama.com), scraping logic powered by `BeautifulSoup`.

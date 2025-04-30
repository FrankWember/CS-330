FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY scraper.py .
COPY sentiment_analyzer.py .
COPY main.py .

# Create output directory
RUN mkdir -p output

CMD ["python", "main.py"]
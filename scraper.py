import requests
from bs4 import BeautifulSoup

# Step 1: Read URLs from input file
try:
    with open("input_urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Error: 'input_urls.txt' not found.")
    exit()

headings = set()

# Step 2: Scrape each URL
for url in urls:
    print(f"\nScraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try grabbing all <h1>, <h2>, and <h3> elements
        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headings.add(text)

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

# Step 3: Save results to output file
try:
    with open("output_headings.txt", "w", encoding="utf-8") as f:
        for h in sorted(headings):
            f.write(h + "\n")
    print(f"\n✅ Wrote {len(headings)} unique headings to 'output_headings.txt'")
except Exception as e:
    print(f"Error writing output file: {e}")

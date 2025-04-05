import requests
from bs4 import BeautifulSoup

# -------------------------------------------
# Step 1: Here, we will read all the URLs from the input file
# -------------------------------------------
# We read all non-empty lines from 'input_urls.txt'.
# Each line should contain one valid news URL to scrape.
# This approach allows easy updating of targets without changing the code.
try:
    with open("input_urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Error: 'input_urls.txt' not found.")
    exit()  # Exit early if the input file doesn't exist

# -------------------------------------------
# Step 2: Initialize a set that will store all the unique headings
# -------------------------------------------
# Using a set automatically removes duplicates, ensuring the output uniqueness.
headings = set()

# -------------------------------------------
# Step 3: Loop through each URL and scrape headings
# -------------------------------------------
# We use requests to fetch the web page and BeautifulSoup to parse HTML content.
# We target <h1>, <h2>, and <h3> tags because they usually contain main page titles and section headers.
for url in urls:
    print(f"\nScraping: {url}")
    try:
        response = requests.get(url, timeout=10)  # timeout prevents hanging
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all heading tags from the page
        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)  # Clean leading/trailing whitespace
            if text:
                headings.add(text)  # Store in set to avoid duplicates

    except Exception as e:
        # If a website fails (e.g., connection error), log and continue
        print(f"Failed to scrape {url}: {e}")

# -------------------------------------------
# Step 4: Here, we will write all cleaned headings to an output file
# -------------------------------------------
# We sort the set before writing to make the output organized and predictable.
# The output is saved to 'output_headings.txt'.
try:
    with open("output_headings.txt", "w", encoding="utf-8") as f:
        for h in sorted(headings):
            f.write(h + "\n")
    print(f"\n✅ Wrote {len(headings)} unique headings to 'output_headings.txt'")
except Exception as e:
    print(f"Error writing output file: {e}")

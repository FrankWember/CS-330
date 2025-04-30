import requests
from bs4 import BeautifulSoup

class BaseScraper:
    def scrape(self):
        raise NotImplementedError

class HeadingScraper(BaseScraper):
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.headings = set()

    def scrape(self):
        try:
            with open(self.input_file, "r") as file:
                urls = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return

        for url in urls:
            print(f"Scraping {url}")
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")
                for tag in soup.find_all(["h1", "h2", "h3"]):
                    text = tag.get_text(strip=True)
                    if text:
                        self.headings.add(text)
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        try:
            with open(self.output_file, "w", encoding="utf-8") as file:
                for heading in sorted(self.headings):
                    file.write(heading + "\n")
            print(f"✅ Saved {len(self.headings)} headings to {self.output_file}")
        except Exception as e:
            print(f"Error writing headings: {e}")

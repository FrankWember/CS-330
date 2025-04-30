from scraper import HeadingScraper
from sentiment_analyzer import LLMSentimentAnalyzer



# Main Program

def main():


    # Scraping headings from provided URLs
    scraper = HeadingScraper(input_file="input_urls.txt", output_file="output/headings.txt")
    scraper.scrape()

    # Step 2: Analyze sentiments of the scraped headings
    analyzer = LLMSentimentAnalyzer(input_file="output/headings.txt", output_file="output/sentiments.txt")
    analyzer.analyze()

if __name__ == "__main__":
    main()

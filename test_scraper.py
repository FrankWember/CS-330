from scraper import HeadingScraper
import os

def test_scraper_creates_output_file():
    input_file = "test_urls.txt"
    output_file = "test_headings.txt"

    # Prepare input
    with open(input_file, "w") as f:
        f.write("https://example.com\n")

    # Fake HTML for test
    fake_html = "<h1>Test Heading</h1>"

    # Patch request.get manually
    import scraper
    def fake_get(*args, **kwargs):
        class Response:
            text = fake_html
        return Response()

    scraper.requests.get = fake_get

    # Run scraper
    scraper = HeadingScraper(input_file, output_file)
    scraper.scrape()

    assert os.path.exists(output_file)
    with open(output_file) as f:
        content = f.read()
    assert "Test Heading" in content

    os.remove(input_file)
    os.remove(output_file)

from sentiment_analyzer import LLMSentimentAnalyzer
import os

def test_sentiment_analyzer_writes_sentiments():
    input_file = "test_headings.txt"
    output_file = "test_sentiments.txt"

    # Prepare headings
    with open(input_file, "w") as f:
        f.write("Something great happened!\n")

    # Patch the LLM call
    import sentiment_analyzer
    def fake_query(*args, **kwargs):
        return "Positive"

    sentiment_analyzer.LLMSentimentAnalyzer.query_model = fake_query

    analyzer = LLMSentimentAnalyzer(input_file, output_file)
    analyzer.analyze()

    with open(output_file) as f:
        sentiment = f.read().strip()

    assert sentiment == "Positive"

    os.remove(input_file)
    os.remove(output_file)

import requests
import random
import os

# Base class for sentiment analyzers
class BaseSentimentAnalyzer:
    def analyze(self):
        raise NotImplementedError("Subclasses must implement the 'analyze' method.")

# Our main analyzer that talks to a local LLM server
class LLMSentimentAnalyzer(BaseSentimentAnalyzer):
    def __init__(self, input_file, output_file, model1="tinyllama", model2="phi3:mini"):
        self.input_file = input_file
        self.output_file = output_file
        self.model1 = model1
        self.model2 = model2
        # Where the LLM server is running
        self.llm_server = os.getenv("LLM_SERVER", "http://localhost:11434")

    def query_model(self, model, prompt):
        """Send a prompt to the LLM and get a response."""
        url = f"{self.llm_server}/api/generate"
        try:
            response = requests.post(
                url,
                json={"model": model, "prompt": prompt, "stream": False},
            )
            data = response.json()
            return data.get("response", "").strip()
        except Exception as e:
            print(f"Couldn't reach LLM server, using random sentiment. Error: {e}")
            return random.choice(["Positive", "Negative", "Neutral"])

    def clean_sentiment(self, text):
        text = text.lower()
        if "positive" in text:
            return "Positive"
        elif "negative" in text:
            return "Negative"
        elif "neutral" in text:
            return "Neutral"
        else:
            return "Neutral"


    def analyze(self):
        """Read headings from input file, analyze sentiments, and save results."""
        # Step 1: Read input headings
        try:
            with open(self.input_file, "r", encoding="utf-8") as file:
                headings = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error reading input file: {e}")
            return

        if not headings:
            print("No headings found in input file.")
            return

        results = []

        # Step 2: Analyze each heading
        for heading in headings:
            prompt = f"Is this heading positive, negative, or neutral? '{heading}'"
            model_response = self.query_model(self.model1, prompt)
            sentiment = self.clean_sentiment(model_response)
            results.append(sentiment)

        # Step 3: Save the sentiments
        try:
            with open(self.output_file, "w", encoding="utf-8") as file:
                file.write("\n".join(results))
            print(f"✅ Done! Saved {len(results)} sentiments to '{self.output_file}'.")
        except Exception as e:
            print(f"Error writing output file: {e}")

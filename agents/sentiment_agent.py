import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

class SentimentAgent:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return sentiment, round(compound, 3)

    def process_dataframe(self, df, text_column="processed_text"):
        sentiments = []
        confidence = []

        for text in df[text_column]:
            s, c = self.analyze_sentiment(text)
            sentiments.append(s)
            confidence.append(c)

        df['sentiment'] = sentiments
        df['confidence'] = confidence
        return df

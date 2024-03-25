import unittest
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class TestVoiceSentimentAnalysis(unittest.TestCase):

    def test_sentiment_analysis(self):
        # Sample text for testing sentiment analysis
        text = "I love this project!"

        # Perform sentiment analysis
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)

        # Check if sentiment score is positive
        self.assertGreater(score['pos'], score['neg'])

    def test_sentiment_analysis(self):
        # Sample text for testing sentiment analysis
        text = "I hate this project!"

        # Perform sentiment analysis
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)

        # Check if sentiment score is negative
        self.assertGreater(score['neg'], score['pos'])


if __name__ == '__main__':
    unittest.main()

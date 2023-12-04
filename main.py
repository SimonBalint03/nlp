import nltk
from textblob import TextBlob

nltk.download('punkt')


def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        words_sentiment = {}

        for word in blob.words:
            word_sentiment = TextBlob(word).sentiment.polarity
            words_sentiment[word] = word_sentiment

        return words_sentiment

    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return None


def analyze_whole_sentence_sentiment(text):
  blob = TextBlob(text)
  sentence_sentiment = blob.sentiment.polarity
  return round(sentence_sentiment * 100)


def dict_of_words_with_given_sentiment(text, sentiment="Negative"):
    try:
        sentiment_analysis = analyze_sentiment(text)
        if sentiment_analysis is None:
            return None

        dict_of_words = {}
        for word, sentiments in sentiment_analysis.items():
            if sentiment == "Negative":
                if sentiments < 0:
                    dict_of_words[word] = sentiments

            if sentiment == "Positive":
                if sentiments > 0:
                    dict_of_words[word] = sentiments
        return dict_of_words

    except Exception as e:
        print(f"Error in creating dictionary of words: {e}")
        return None


##################### TEST CASE ####################################################
def main():
    try:
        SAMPLE_TEXT = """
I hope this message finds you well. I wanted to take a moment to express my heartfelt appreciation for the exceptional work you've been doing recently. Your contributions have been nothing short of outstanding!

The dedication and attention to detail you bring to your projects have not gone unnoticed. Your recent work on [specific project] showcased a level of excellence that truly sets a high standard for the team. Clients have provided glowing feedback, emphasizing how your efforts have significantly contributed to the success of our endeavors.

Your positive attitude, collaborative spirit, and commitment to delivering top-notch results have made a significant impact. I am genuinely impressed with your work ethic and the quality of your output.

Keep up the fantastic work! Your contributions are invaluable to the success of our team and the company as a whole. If you have any thoughts or ideas you'd like to share, I'm always here to listen.

Once again, thank you for your outstanding efforts!

Best regards,
        """

        print(analyze_sentiment(SAMPLE_TEXT))
        print("Positive:")
        print(dict_of_words_with_given_sentiment(SAMPLE_TEXT, sentiment="Positive"))
        print("Negative:")
        print( dict_of_words_with_given_sentiment(SAMPLE_TEXT, sentiment="Negative"))
        print(analyze_whole_sentence_sentiment(SAMPLE_TEXT), "%")

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == '__main__':
    main()

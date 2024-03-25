from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyaudio
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Clearing background noise....')
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print('Speak now....')
    recordedaudio = recognizer.listen(source)
    print('Message recorded...!')


try:
    print('Printing the recorded message...')
    text = recognizer.recognize_google(recordedaudio, language='en-US')
    print(text)
except Exception as ex:
    print(ex)


# Sentiment Analysis

Sentence = [str(text)]
analyzer = SentimentIntensityAnalyzer()
for i in Sentence:
    score = analyzer.polarity_scores(text)
    print(score)

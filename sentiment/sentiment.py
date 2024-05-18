from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    
    print(f'Text: {text}')
    print(f'Sentimiento: {sentiment}')
    print(f'Polaridad: {polarity}')

text_example = 'i hate you so much franko, you are the life!'
analyze_sentiment(text_example)    
from google_news_feed import GoogleNewsFeed
from flask import Flask, render_template
from transformers import pipeline

app = Flask(__name__)




negative_words = [
    'abandon', 'abandoned', 'abandoning',
    'accuse', 'accused', 'accusing', 'accusation',
    'afraid', 'aggravate', 'aggravated', 'aggravating', 'aggravation',
    'alarm', 'alarmed', 'alarming',
    'anger', 'angered', 'angry',
    'annoy', 'annoyed', 'annoying', 'annoyance',
    'anxiety', 'anxious', 'apprehension', 'apprehensive',
    'argue', 'argued', 'arguing', 'argument',
    'attack', 'attacked', 'attacking',
    'bad', 'badly',
    'bankrupt', 'bankruptcy', 'bankrupted',
    'blame', 'blamed', 'blaming',
    'bleak', 'bleakness',
    'collapse', 'collapsed', 'collapsing',
    'complain', 'complained', 'complaining', 'complaint',
    'conflict', 'conflicted', 'conflicting',
    'crash', 'crashed', 'crashing',
    'crime', 'criminal', 'criminals',
    'crisis', 'critical', 'criticism', 'criticize', 'criticized', 'criticizing',
    'damage', 'damaged', 'damaging',
    'danger', 'dangerous', 'dangerously',
    'decline', 'declined', 'declining',
    'defeat', 'defeated', 'defeating',
    'deficit', 'deficient',
    'delay', 'delayed', 'delaying',
    'deny', 'denied', 'denying', 'denial',
    'depress', 'depressed', 'depressing', 'depression',
    'destroy', 'destroyed', 'destroying', 'destruction',
    'devastate', 'devastated', 'devastating', 'devastation',
    'disaster', 'disastrous', 'disastrously',
    'displace', 'displaced', 'displacing', 'displacement',
    'dispute', 'disputed', 'disputing',
    'dissolve', 'dissolved', 'dissolving',
    'downturn', 'downward',
    'dread', 'dreaded', 'dreadful', 'dreading',
    'drought',
    'drop', 'dropped', 'dropping',
    'fail', 'failed', 'failing', 'failure',
    'fear', 'feared', 'fearing', 'fearful',
    'fraud', 'fraudulent',
    'frighten', 'frightened', 'frightening',
    'guilty', 'guilt',
    'harm', 'harmed', 'harming', 'harmful',
    'hate', 'hated', 'hating', 'hatred',
    'injure', 'injured', 'injuring', 'injury',
    'insult', 'insulted', 'insulting',
    'kill','killing','killed',
    'loss', 'lost', 'losing',
    'mistake', 'mistaken', 'mistaking',
    'murder','murdering','murderer','murdered',
    'neglect', 'neglected', 'neglecting', 'negligence', 'negligent',
    'panic', 'panicked', 'panicking',
    'pollute', 'polluted', 'polluting', 'pollution',
    'problem', 'problematic',
    'recession', 'recessive',
    'reject', 'rejected', 'rejecting', 'rejection',
    'risk', 'risky', 'risking',
    'scandal', 'scandalous',
    'shortage', 'shortfall',
    'suffer', 'suffered', 'suffering', 'suffers',
    'terror', 'terrorism', 'terrorist', 'terrorists',
    'threat', 'threaten', 'threatened', 'threatening',
    'tragedy', 'tragic',
    'unemploy', 'unemployed', 'unemployment',
    'violence', 'violent', 'violently',
    'war', 'warfare', 'warred', 'warring',
    'worry', 'worried', 'worrying',
    'wound', 'wounded', 'wounding'
]






# Load the pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Function to classify sentiment of a sentence
def classify_sentiment(sentence):
    result = sentiment_pipeline(sentence)
    sentiment = result[0]['label']
    confidence = result[0]['score']
    return sentiment, confidence


@app.route("/")
def index():
    gnf = GoogleNewsFeed(language='en',country='US')
    results = gnf.top_headlines()

    positive_headlines = []
    
    for headline in results:
        sentiment, confidence = classify_sentiment(headline.title)
        if sentiment == "POSITIVE" and confidence > 0.9:
            for word in headline.title.split():
                if word.lower() in negative_words:
                    break
            else:
                positive_headlines.append({'title': headline.title, 'link': headline.link})

    return render_template('index.html',headlines=positive_headlines)

if __name__ == '__main__':
    app.run(debug=True)

User_Analysis_script.py
import tweepy
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import json
import random
from datetime import datetime, timedelta

# Mock data for environment variables
os.environ['X_API_KEY'] = 'simulated_api_key'
os.environ['X_API_SECRET'] = 'simulated_api_secret'
os.environ['X_ACCESS_TOKEN'] = 'simulated_access_token'
os.environ['X_ACCESS_TOKEN_SECRET'] = 'simulated_access_token_secret'

# Download necessary NLTK data
nltk.download('vader_lexicon', quiet=True)

def get_twitter_api():
    auth = tweepy.OAuthHandler(os.environ['X_API_KEY'], os.environ['X_API_SECRET'])
    auth.set_access_token(os.environ['X_ACCESS_TOKEN'], os.environ['X_ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    vader_sentiment = sia.polarity_scores(text)
    textblob_sentiment = TextBlob(text).sentiment
    
    return {
        'vader': vader_sentiment,
        'textblob': {
            'polarity': textblob_sentiment.polarity,
            'subjectivity': textblob_sentiment.subjectivity
        }
    }

def generate_simulated_tweet():
    simulated_tweets = [
        "Feeling super excited for the weekend! #FridayVibes",
        "Another day at the office, can't wait for this project to be over.",
        "Just had the best avocado toast ever 🥑🍞",
        "Why does it always rain when I forget my umbrella? ☔",
        "Adopting a new puppy today! 🐶 #PetLove"
    ]
    return random.choice(simulated_tweets)

def generate_simulated_tweets(count):
    tweets = []
    for i in range(count):
        tweet = generate_simulated_tweet()
        tweets.append({
            'id_str': f"tweet_id_{i}",
            'created_at': (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
            'full_text': tweet
        })
    return tweets

def analyze_tweets(api, user_id):
    # Instead of fetching real tweets, we generate simulated ones for this demo
    tweets = generate_simulated_tweets(200)  # Simulate 200 tweets
    analysis_results = []
    
    for tweet in tweets:
        sentiment_scores = analyze_sentiment(tweet['full_text'])
        analysis_results.append({
            'tweet_id': tweet['id_str'],
            'created_at': tweet['created_at'],
            'text': tweet['full_text'],
            'sentiment': sentiment_scores
        })
    
    compound_scores = [tweet['sentiment']['vader']['compound'] for tweet in analysis_results]
    average_sentiment = sum(compound_scores) / len(compound_scores) if compound_scores else 0
    
    return {
        'tweets': analysis_results,
        'average_sentiment': average_sentiment
    }

def main():
    api = get_twitter_api()  # This will use the simulated credentials
    user_id = input("Enter Twitter username: ") or 'example_user'
    
    try:
        results = analyze_tweets(api, user_id)
        
        # Save results to a JSON file
        with open('tweet_analysis.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Analysis completed for user {user_id}. Results saved to 'tweet_analysis.json'.")
        print(f"Average sentiment score: {results['average_sentiment']:.2f}")
        
    except tweepy.TweepError as e:
        print(f"An error occurred while fetching tweets: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

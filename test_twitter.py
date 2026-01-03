# filepath: d:\AK_105\Hate _speech_detection\test_twitter.py
import snscrape.modules.twitter as sntwitter

def fetch_tweets(username, limit=5):
    tweets = []
    try:
        for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
            if i >= limit:
                break
            tweets.append(tweet.content)
    except Exception as e:
        print(f"Error: {e}")
    return tweets

if __name__ == "__main__":
    username = "elonmusk"
    tweets = fetch_tweets(username, limit=5)

    if tweets:
        print(f"✅ Retrieved {len(tweets)} tweets from @{username}")
        for i, t in enumerate(tweets, start=1):
            print(f"{i}. {t}\n")
    else:
        print(f"⚠️ No tweets found for @{username}")
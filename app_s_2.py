import streamlit as st
import tweepy
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

# Load smaller, faster model (cached)
@st.cache_resource
def load_classifier():
    # DistilBERT is ~6x faster and ~250MB vs ~1.6GB for BART-large
    return pipeline(
        "zero-shot-classification",
        model="typeform/distilbert-base-uncased-mnli",
        framework="pt"
    )

classifier = load_classifier()

# Candidate labels
CATEGORIES = ["hate", "offensive", "spam", "happy", "neutral"]

# -------------------------
# Twitter API Authentication
# -------------------------
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
twitter_client = None
if BEARER_TOKEN:
    twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN)

# -------------------------
# Function: classify text
# -------------------------
def classify_text(text):
    result = classifier(text, candidate_labels=CATEGORIES)
    label = result["labels"][0]
    score = result["scores"][0]
    return f"{label} ({score:.2f})"

# -------------------------
# Function: styled card
# -------------------------
def create_card(tweet_text, prediction):
    color_map = {
        "hate": ("#DC143C", "🚫"),        # crimson
        "offensive": ("#FF8C00", "⚠️"),   # dark orange
        "spam": ("#800080", "📢"),        # purple
        "happy": ("#32CD32", "😄"),       # lime green
        "neutral": ("#708090", "😐")      # slate gray
    }
    label = prediction.split()[0].lower()
    color, emoji = color_map.get(label, ("#ADD8E6", "❔"))

    # Choose text color for contrast
    text_color = "white"

    card_html = f"""
    <div style="background-color: {color}; padding: 12px; border-radius: 8px; margin: 10px 0;">
        <h5 style="color: {text_color};">{emoji} Prediction: {prediction}</h5>
        <p style="color: {text_color};">{tweet_text}</p>
    </div>
    """
    return card_html

# -------------------------
# Main Streamlit App
# -------------------------
def main():
    st.title("Tweet Classification App 🚀")
    st.write("Classify tweets into categories: **hate, offensive, spam, happy, neutral**")
    st.write("Using: `distilbert-base-uncased-mnli` (fast & lightweight)")

    # Input mode selection
    st.subheader("Choose Input Method")
    option = st.radio(
        "Select how you want to provide input:",
        ["📝 Enter Text Manually", "🐦 Fetch Tweets from Twitter"],
        horizontal=True
    )

    # ----------------------------------
    # Option 1: Manual Text Input
    # ----------------------------------
    if option == "📝 Enter Text Manually":
        st.markdown("---")
        text_input = st.text_area("Enter text to classify", height=100)
        
        if st.button("🔍 Classify Text", type="primary"):
            if text_input.strip():
                with st.spinner("Classifying..."):
                    prediction = classify_text(text_input)
                st.markdown(create_card(text_input, prediction), unsafe_allow_html=True)
            else:
                st.warning("Please enter some text.")

    # ----------------------------------
    # Option 2: Fetch Tweets from Twitter
    # ----------------------------------
    elif option == "🐦 Fetch Tweets from Twitter":
        st.markdown("---")
        
        if not twitter_client:
            st.error("⚠️ Twitter API credentials not found! Please add `TWITTER_BEARER_TOKEN` to your `.env` file.")
            st.info("""
            **How to get Twitter API credentials:**
            1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
            2. Create a project and an app
            3. Generate a Bearer Token
            4. Add it to your `.env` file as: `TWITTER_BEARER_TOKEN=your_token_here`
            """)
            return

        col1, col2 = st.columns([2, 1])
        
        with col1:
            username = st.text_input("Enter Twitter username (without @)", placeholder="elonmusk")
        
        with col2:
            num_tweets = st.slider("Number of tweets", min_value=5, max_value=100, value=10, step=5)

        if st.button("🚀 Fetch and Classify Tweets", type="primary"):
            if not username.strip():
                st.warning("Please enter a Twitter username.")
                return

            try:
                with st.spinner(f"Fetching tweets from @{username}..."):
                    # Get user info
                    user_data = twitter_client.get_user(username=username)
                    
                    if not user_data.data:
                        st.error(f"❌ No user found with username @{username}")
                        return

                    # Fetch tweets
                    tweets = twitter_client.get_users_tweets(
                        id=user_data.data.id,
                        max_results=num_tweets,
                        tweet_fields=["text", "created_at"]
                    )

                    if tweets.data:
                        st.success(f"✅ Found {len(tweets.data)} tweets from @{username}")
                        st.markdown("---")
                        
                        # Classify each tweet
                        progress_bar = st.progress(0)
                        for i, tweet in enumerate(tweets.data):
                            tweet_text = tweet.text
                            prediction = classify_text(tweet_text)
                            st.markdown(create_card(tweet_text, prediction), unsafe_allow_html=True)
                            progress_bar.progress((i + 1) / len(tweets.data))
                        
                        progress_bar.empty()
                    else:
                        st.warning("⚠️ No tweets found for this user.")

            except tweepy.TooManyRequests:
                st.error("⚠️ Rate limit reached. Please wait a few minutes and try again.")
            except tweepy.Unauthorized:
                st.error("⚠️ Twitter API authentication failed. Please check your Bearer Token.")
            except tweepy.NotFound:
                st.error(f"❌ User @{username} not found.")
            except Exception as e:
                st.error(f"❌ Error fetching tweets: {str(e)}")

    # Footer
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit, Transformers & Twitter API")

if __name__ == "__main__":
    main()

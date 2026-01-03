import re
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Same exclusions from your Colab
exclusions = ["#ff", "ff", "rt", "\"\"\""]

# Regex patterns (exactly like Colab)
char_regExp = r"[,\?:\|]"
quoteHtml_regExp = r"(&#8220;)|(&#8221;)"
andHtml_regExp = r"(&amp;)"
emo_regExp = r"&#(\d+);"
space_pattern = r"\s+"
giant_url_regex = r"http[s]?://\S+"
mention_regex = r"@[\w\-]+"

# Dummy clean function (you had it in Colab but not defined)
def clean(text: str) -> str:
    # If you didn’t have extra logic, just lowercase
    return text.lower()

# Dummy segment function (you had it in Colab but not defined)
def segment(text: str) -> list:
    # If no special segmentation, just split words
    return text.split()

# Main preprocessing function
def preprocess(tweet: str) -> str:
    tweet = re.sub(space_pattern, " ", tweet)       # remove extra spaces
    tweet = re.sub(giant_url_regex, "", tweet)      # remove URLs
    tweet = re.sub(mention_regex, "", tweet)        # remove @mentions
    tweet = re.sub(char_regExp, "", tweet)          # remove punctuation
    tweet = re.sub(quoteHtml_regExp, "", tweet)     # remove encoded quotes
    tweet = re.sub(andHtml_regExp, "", tweet)       # remove '&' HTML
    tweet = re.sub(emo_regExp, "", tweet)           # remove emojis

    tweet = clean(tweet)       # custom cleaning
    words = segment(tweet)     # word segmentation
    filtered_tokens = [w for w in words if w not in exclusions]
    lemmatized_tokens = [lemmatizer.lemmatize(t) for t in filtered_tokens]
    tweet = " ".join(lemmatized_tokens)
    return tweet

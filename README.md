# 🚫 Hate Speech Detection App

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![Transformers](https://img.shields.io/badge/🤗_Transformers-Latest-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

<!-- 🖼️ IMAGE 1: Add a banner/header image here -->
<!-- ![Banner](images/banner.png) -->

A powerful AI-powered application that classifies text and tweets into categories: **Hate**, **Offensive**, **Spam**, **Happy**, and **Neutral** using DistilBERT zero-shot classification.

---

## ✨ Features

- 🔍 **Text Classification** - Classify any text input instantly
- 🐦 **Twitter Integration** - Fetch and analyze tweets from any public Twitter account
- ⚡ **Fast Inference** - Uses DistilBERT (6x faster than BART-large)
- 🎨 **Beautiful UI** - Color-coded results with emoji indicators
- 📊 **Real-time Progress** - Progress bar for batch tweet analysis

---

## 📸 Screenshots

<!-- 🖼️ IMAGE 2: Main app interface screenshot -->
### Main Interface
<!-- ![Main Interface](images/main_interface.png) -->
*Add screenshot of the main app interface here*

<!-- 🖼️ IMAGE 3: Text classification result -->
### Text Classification
<!-- ![Text Classification](images/text_classification.png) -->
*Add screenshot showing text classification result here*

<!-- 🖼️ IMAGE 4: Twitter analysis results -->
### Twitter Analysis
<!-- ![Twitter Analysis](images/twitter_analysis.png) -->
*Add screenshot showing Twitter analysis results here*

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web application framework |
| **Hugging Face Transformers** | NLP model for classification |
| **Tweepy** | Twitter API integration |
| **DistilBERT** | Zero-shot classification model |

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Twitter Developer Account (for Twitter features)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AKASH-C-105/hate-speech-detection.git
   cd hate-speech-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
   ```

   > 💡 **Get Twitter API credentials:**
   > 1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
   > 2. Create a project and app
   > 3. Generate a Bearer Token

---

## 📖 Usage

### Run the Application

```bash
streamlit run app_s_2.py
```

The app will open in your browser at `http://localhost:8501`

### Option 1: Manual Text Classification

1. Select "📝 Enter Text Manually"
2. Type or paste your text
3. Click "🔍 Classify Text"

### Option 2: Twitter Analysis

1. Select "🐦 Fetch Tweets from Twitter"
2. Enter a Twitter username (without @)
3. Choose number of tweets to analyze
4. Click "🚀 Fetch and Classify Tweets"

---

## 📁 Project Structure

```
hate-speech-detection/
├── 📄 app_s_2.py           # Main Streamlit application
├── 📄 test_twitter.py      # Twitter API testing script
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env                 # Environment variables (not tracked)
├── 📄 .gitignore           # Git ignore rules
│
├── 📁 models/              # Trained models and weights
├── 📁 data/                # Dataset files
├── 📁 notebook/            # Jupyter notebooks for experiments
├── 📁 templates/           # HTML templates
└── 📁 utils/               # Utility functions
    └── preprocess.py       # Text preprocessing utilities
```

---

## 🎯 Classification Categories

| Category | Color | Emoji | Description |
|----------|-------|-------|-------------|
| **Hate** | 🔴 Crimson | 🚫 | Hateful or discriminatory content |
| **Offensive** | 🟠 Orange | ⚠️ | Offensive or inappropriate language |
| **Spam** | 🟣 Purple | 📢 | Promotional or spam content |
| **Happy** | 🟢 Green | 😄 | Positive or joyful content |
| **Neutral** | ⚪ Gray | 😐 | Neutral or informational content |

---

## 🔧 Model Information

- **Model**: `typeform/distilbert-base-uncased-mnli`
- **Type**: Zero-shot classification
- **Size**: ~250MB (6x smaller than BART-large)
- **Speed**: ~6x faster inference

---

## 📊 Demo

<!-- 🖼️ IMAGE 5: GIF showing app demo -->
<!-- ![Demo GIF](images/demo.gif) -->
*Add a GIF demonstrating the app workflow here*

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**AKASH C**

- GitHub: [@AKASH-C-105](https://github.com/AKASH-C-105)

---

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Twitter/X](https://developer.twitter.com/) for the API access

---

<p align="center">
  Built with ❤️ using Streamlit, Transformers & Twitter API
</p>

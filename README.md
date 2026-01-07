# Sentilytics
dvanced sentiment analysis app with dual ML models (TF-IDF + BERT) achieving 93% accuracy. Interactive Streamlit dashboard for analyzing customer reviews.

# 🧠 Advanced Sentiment Analysis App

A comprehensive sentiment analysis tool that combines traditional machine learning with modern transformer models to analyze customer reviews and feedback.

## 🌟 What This App Does

Ever wondered what customers really think beyond just star ratings? This app digs deeper into review text to uncover the true sentiment, helping businesses understand their customers better.

**Key Features:**
- Upload CSV files with customer reviews
- Choose between TF-IDF + Logistic Regression or BERT models
- Generate beautiful visualizations (word clouds, sentiment distribution)
- Identify misleading high-rated reviews with negative sentiment
- Track sentiment trends over time
- Download analyzed results as CSV

## 🚀 Live Demo

The app is built with Streamlit and provides an interactive web interface where you can:
- Upload your own review data
- Switch between different AI models
- See real-time analysis results
- Export processed data

## 🛠️ Tech Stack

**Frontend:**
- Streamlit for the web interface
- Matplotlib & Seaborn for visualizations
- WordCloud for text visualization

**ML Models:**
- **Traditional ML**: TF-IDF vectorization + Logistic Regression (93% accuracy)
- **Deep Learning**: BERT (Multilingual) from HuggingFace Transformers
- Natural Language Processing with NLTK

**Data Processing:**
- Pandas for data manipulation
- Regex for text cleaning
- Scikit-learn for traditional ML pipeline

## 📊 Model Performance

Our TF-IDF + Logistic Regression model achieves **93% accuracy** on test data, making it reliable for real-world sentiment analysis tasks.

The BERT model provides more nuanced understanding of context and handles multilingual reviews better.

## 🏃‍♂️ Quick Start

### Installation

```bash
git clone https://github.com/yourusername/sentiment-analyzer-app
cd sentiment-analyzer-app
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Using Your Own Data

Your CSV file should have a `reviewText` column. Optional columns:
- `overall` - star ratings (1-5)
- `reviewTime` - for time-based analysis

Example CSV structure:
```csv
reviewText,overall,reviewTime
"Great product, loved it!",5,2023-01-15
"Not what I expected...",2,2023-01-20
```

## 📁 Project Structure

```
sentiment-analyzer-app/
├── app.py                      # Main Streamlit application
├── sentiment-analysis-pro-01.ipynb  # Model training notebook
├── sentiment_model.pkl         # Trained TF-IDF model
├── tfidf_vectorizer.pkl       # Fitted vectorizer
├── requirements.txt           # Python dependencies
└── README.md                  # You're reading it!
```

## 🔍 How It Works

### 1. Text Preprocessing
- Converts text to lowercase
- Removes HTML tags and special characters
- Eliminates stopwords
- Tokenizes and cleans the text

### 2. Sentiment Classification
```python
def map_sentiment(score):
    if score <= 2.5:
        return 'negative'
    elif score <= 3.5:
        return 'neutral' 
    else:
        return 'positive'
```

### 3. Model Options
- **TF-IDF + LogisticRegression**: Fast, reliable, works offline
- **BERT**: More accurate, understands context better

### 4. Visualizations
- Sentiment distribution bar charts
- Word clouds for positive/negative reviews
- Time-based trend analysis
- Misleading review detection

## 💡 Key Insights This App Reveals

**Hidden Problems:** Sometimes 5-star rated products have hidden negative sentiments that traditional ratings miss.

**Trend Analysis:** See how customer sentiment changes over time, even when star ratings stay stable.

**Word Patterns:** Discover what specific words customers use when they're happy vs unhappy.

## 🎯 Use Cases

- **E-commerce**: Analyze product reviews to improve customer satisfaction
- **Social Media**: Monitor brand sentiment across platforms  
- **Market Research**: Understand customer opinions at scale
- **Product Development**: Identify pain points from user feedback

## 🧪 Training Process

The model was trained on Amazon review data with:
- Text cleaning and preprocessing
- TF-IDF vectorization (5000 features)
- 3-class classification (positive/neutral/negative)
- Train-test split (80/20)
- Achieved 93% accuracy on test set

## 🤖 Models Explained

### TF-IDF + Logistic Regression
- **Pros**: Fast, interpretable, works offline
- **Cons**: Doesn't understand context as well
- **Best for**: Large-scale batch processing

### BERT (Transformers)
- **Pros**: Understands context, very accurate, multilingual
- **Cons**: Slower, requires more resources
- **Best for**: High-accuracy requirements

## 🔮 Future Improvements

- Add aspect-based sentiment analysis (price, quality, service)
- Support for more languages
- Real-time social media sentiment tracking
- API endpoint for integration with other apps
- Mobile-responsive design

## 📈 Sample Results

The app successfully identifies cases where:
- 5-star reviews contain negative sentiment about specific aspects
- Overall sentiment trends differ from rating trends
- Specific pain points emerge from customer feedback

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Some areas for improvement:
- Adding more visualization types
- Implementing new ML models
- Improving the UI/UX
- Adding export options

## 📄 License

MIT License - Feel free to use this for your own projects!
##Images 
<img width="2457" height="1075" alt="image" src="https://github.com/user-attachments/assets/36bc37a7-965c-4a5e-b734-71443e2d9a19" />
<img width="1106" height="892" alt="image" src="https://github.com/user-attachments/assets/5516b4e4-d805-4eec-905e-7fad6fa7a85b" />
<img width="1054" height="1192" alt="image" src="https://github.com/user-attachments/assets/3b11584b-71e6-493d-a741-47704b13c664" />
<img width="1094" height="1245" alt="image" src="https://github.com/user-attachments/assets/80d423ea-a049-4637-b762-ca8b9a68799a" />
<img width="1104" height="1237" alt="image" src="https://github.com/user-attachments/assets/17de3041-4eaf-46f1-9356-6d4c334f96fb" />




---

*Built with Python, Streamlit, and a lot of coffee ☕*

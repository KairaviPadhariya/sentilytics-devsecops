# Import necessary libraries
import os
import streamlit as st
import pandas as pd
import pickle
import re
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax

# Download stopwords from NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Configure Streamlit page settings
st.set_page_config(page_title="Sentilytics - Sentiment Analysis Dashboard", layout="wide")

# Custom CSS for modern visual styling
st.markdown("""
    <style>
    /* Gradient title container */
    .title-container {
        padding: 2rem;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    .title-main {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        font-family: 'Outfit', 'Inter', sans-serif;
    }
    .title-sub {
        font-size: 1.1rem;
        opacity: 0.85;
        margin-top: 5px;
        font-weight: 400;
    }
    
    /* Metrics panel styling */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #eef2f6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
    }
    
    /* Info Card style */
    .info-card {
        padding: 25px;
        background-color: #ffffff;
        border-radius: 12px;
        border-left: 5px solid #2a5298;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        margin-bottom: 1.5rem;
    }
    .info-card h3 {
        margin-top: 0;
        color: #1e3c72;
    }
    </style>
""", unsafe_allow_html=True)

# Render Beautiful Gradient Header
st.markdown("""
<div class="title-container">
    <div class="title-main">🧠 Sentilytics Dashboard</div>
    <div class="title-sub">DevSecOps-Enabled Sentiment Prediction & Analytics</div>
</div>
""", unsafe_allow_html=True)

# Sidebar layout
st.sidebar.markdown("### 🧠 Sentilytics")
st.sidebar.caption("DevSecOps · Sentiment Analysis")
st.sidebar.markdown("---")

st.sidebar.subheader("📂 Data Source")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file with reviews", type=["csv"])
use_sample = st.sidebar.checkbox("Use Sample Reviews Dataset", value=False)

# Sidebar model configuration
st.sidebar.subheader("🤖 Model Settings")
model_choice = st.sidebar.selectbox("Choose a model:", ["TF-IDF + LogisticRegression", "BERT (Transformers)"])

# Sidebar instructions
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📖 How to use
1. **Load Data**: Upload a CSV file containing a `reviewText` column or check the sample dataset checkbox.
2. **Select Model**: Choose between a fast traditional ML model (**TF-IDF + LR**) or a context-aware Deep Learning model (**BERT**).
3. **Explore tabs**:
   - **Overview**: View metrics & sample annotated data.
   - **Word Clouds**: Identify most frequent words.
   - **Review Explorer**: Search and filter reviews.
   - **Trend Analysis**: Monitor ratings & sentiments over time.
""")

# Function to clean and preprocess review text
def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()  # Lowercase text
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # Remove non-letter characters
    text = text.split()  # Tokenize
    text = [word for word in text if word not in stop_words]  # Remove stopwords
    return ' '.join(text)

# Function to map numeric star ratings to sentiment labels
def map_sentiment(score):
    if score <= 2.5:
        return 'negative'
    elif score <= 3.5:
        return 'neutral'
    else:
        return 'positive'

# Load pretrained BERT model and tokenizer with caching
@st.cache_resource
def load_bert():
    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    return tokenizer, model

# Predict sentiment using BERT model
def predict_bert(texts, tokenizer, model):
    sentiments = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item() + 1  # Class index shifted from 0–4 to 1–5
        # Map prediction to sentiment
        if pred <= 2:
            sentiments.append("negative")
        elif pred == 3:
            sentiments.append("neutral")
        else:
            sentiments.append("positive")
    return sentiments

# Check if data source is available
if uploaded_file is not None or use_sample:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("File uploaded successfully!")
    else:
        df = pd.read_csv("sample_reviews.csv")
        st.sidebar.info("Using sample reviews dataset.")

    # Check for required 'reviewText' column
    if 'reviewText' not in df.columns:
        st.error("The dataset must have a 'reviewText' column.")
    else:
        # Clean the review text
        df['cleaned'] = df['reviewText'].apply(clean_text)

        # Map numeric ratings to sentiment if 'overall' column is present
        if 'overall' in df.columns:
            df['true_sentiment'] = df['overall'].apply(map_sentiment)

        # Execute predictions depending on selected model
        if model_choice == "TF-IDF + LogisticRegression":
            MODEL_PATH = os.path.join(os.getcwd(), "sentiment_model.pkl")
            VECTORIZER_PATH = os.path.join(os.getcwd(), "tfidf_vectorizer.pkl")

            # Show system debug metrics inside sidebar expander
            with st.sidebar.expander("🛠️ System Debug Information"):
                st.write("Current Working Directory:", os.getcwd())
                st.write("Files in Current Directory:", os.listdir())
                st.write("Model File Exists:", os.path.exists(MODEL_PATH))
                st.write("Vectorizer File Exists:", os.path.exists(VECTORIZER_PATH))

            model = pickle.load(open(MODEL_PATH, "rb"))
            vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))   
            X = vectorizer.transform(df['cleaned'])
            df['sentiment'] = model.predict(X)

        elif model_choice == "BERT (Transformers)":
            with st.sidebar.expander("🛠️ System Debug Information"):
                st.write("Current Working Directory:", os.getcwd())
                st.write("Files in Current Directory:", os.listdir())

            with st.spinner("Loading BERT model and analyzing text. Please wait..."):
                tokenizer, bert_model = load_bert()
                df['sentiment'] = predict_bert(df['reviewText'].astype(str).tolist(), tokenizer, bert_model)

        # Export predictions button in the sidebar
        st.sidebar.markdown("---")
        st.sidebar.subheader("📥 Export Results")
        st.sidebar.download_button(
            label="Download Annotated CSV",
            data=df.to_csv(index=False),
            file_name="annotated_reviews.csv",
            mime="text/csv"
        )

        # High-level metrics calculations
        total_reviews = len(df)
        sentiment_counts = df['sentiment'].value_counts()
        
        pos_count = sentiment_counts.get('positive', 0)
        neu_count = sentiment_counts.get('neutral', 0)
        neg_count = sentiment_counts.get('negative', 0)
        
        pos_pct = (pos_count / total_reviews) * 100 if total_reviews > 0 else 0
        neu_pct = (neu_count / total_reviews) * 100 if total_reviews > 0 else 0
        neg_pct = (neg_count / total_reviews) * 100 if total_reviews > 0 else 0

        # Metric Cards Layout
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        m_col1.metric("Total Reviews", f"{total_reviews:,}")
        m_col2.metric("Positive Sentiment", f"{pos_pct:.1f}%", f"{pos_count} reviews")
        m_col3.metric("Neutral Sentiment", f"{neu_pct:.1f}%", f"{neu_count} reviews")
        m_col4.metric("Negative Sentiment", f"{neg_pct:.1f}%", f"{neg_count} reviews", delta_color="inverse")

        st.write("")

        # Create Tabbed Dashboard
        tab_overview, tab_wordcloud, tab_explorer, tab_trends = st.tabs([
            "📊 Overview & Stats",
            "☁️ Word Clouds",
            "🔎 Review Explorer",
            "📅 Trend Analysis"
        ])

        # Overview Tab
        with tab_overview:
            st.subheader("📊 Sentiment Distribution")
            o_col1, o_col2 = st.columns([2, 1])
            with o_col1:
                # Format counts for clean display in st.bar_chart
                chart_data = pd.DataFrame({
                    "Reviews Count": [pos_count, neu_count, neg_count]
                }, index=["Positive", "Neutral", "Negative"])
                st.bar_chart(chart_data)
            with o_col2:
                st.markdown("""
                <div class="info-card">
                    <h4>About the Model</h4>
                    <p>Predicted using <b>{}</b>.</p>
                    <p>The sentiment is derived by analyzing the text patterns and mapping them to three categories:</p>
                    <ul>
                        <li><b>Positive:</b> Satisfied and enthusiastic reviews.</li>
                        <li><b>Neutral:</b> Mixed, informative, or middle-ground reviews.</li>
                        <li><b>Negative:</b> Critical, disappointed, or issue-reporting reviews.</li>
                    </ul>
                </div>
                """.format(model_choice), unsafe_allow_html=True)

            st.subheader("📋 Annotated Reviews Sample (Top 10)")
            st.dataframe(df[['reviewText', 'sentiment']].head(10), use_container_width=True)

        # Word Clouds Tab
        with tab_wordcloud:
            st.subheader("☁️ Word Clouds Analysis")
            st.write("Visualize the most frequent words in positive and negative reviews.")
            
            pos_text = ' '.join(df[df['sentiment'] == 'positive']['cleaned'])
            neg_text = ' '.join(df[df['sentiment'] == 'negative']['cleaned'])
            
            w_col1, w_col2 = st.columns(2)
            
            with w_col1:
                st.markdown("##### Positive Review Keywords")
                if pos_text.strip():
                    wordcloud_pos = WordCloud(width=600, height=400, background_color='white', colormap='Greens').generate(pos_text)
                    st.image(wordcloud_pos.to_array(), use_column_width=True)
                else:
                    st.warning("Not enough positive reviews to generate a word cloud.")
                    
            with w_col2:
                st.markdown("##### Negative Review Keywords")
                if neg_text.strip():
                    wordcloud_neg = WordCloud(width=600, height=400, background_color='black', colormap='Reds').generate(neg_text)
                    st.image(wordcloud_neg.to_array(), use_column_width=True)
                else:
                    st.warning("Not enough negative reviews to generate a word cloud.")

        # Review Explorer Tab
        with tab_explorer:
            st.subheader("🕵️ Review Filter & Inspector")
            filter_sentiment = st.radio(
                "Filter by sentiment category:",
                ["positive", "neutral", "negative"],
                horizontal=True
            )
            filtered_df = df[df['sentiment'] == filter_sentiment]
            st.write(f"Showing **{len(filtered_df)}** reviews classified as **{filter_sentiment}**:")
            st.dataframe(filtered_df[['reviewText', 'sentiment']], use_container_width=True)

            if 'overall' in df.columns:
                st.markdown("---")
                st.subheader("⚠️ Misleading 5-Star Reviews")
                st.write("Reviews with high overall ratings (e.g. 5 stars) but containing negative or neutral predicted sentiments:")
                misleading = df[(df['overall'] >= 5) & (df['sentiment'] != 'positive')]
                if not misleading.empty:
                    st.warning(f"Found {len(misleading)} potentially misleading reviews.")
                    st.dataframe(misleading[['reviewText', 'overall', 'sentiment']], use_container_width=True)
                else:
                    st.success("No misleading 5-star reviews detected.")

        # Trend Analysis Tab
        with tab_trends:
            if 'reviewTime' in df.columns:
                st.subheader("📅 Temporal Trends")
                
                df['reviewTime'] = pd.to_datetime(df['reviewTime'], errors='coerce')
                df = df.dropna(subset=['reviewTime'])

                time_freq = st.selectbox("Select time resolution:", ['Month', 'Week', 'Day'])

                # Create time periods
                if time_freq == 'Month':
                    df['time_period'] = df['reviewTime'].dt.to_period('M').dt.to_timestamp()
                elif time_freq == 'Week':
                    df['time_period'] = df['reviewTime'].dt.to_period('W').dt.to_timestamp()
                else:
                    df['time_period'] = df['reviewTime'].dt.date

                t_col1, t_col2 = st.columns(2)
                
                with t_col1:
                    st.markdown("##### 📈 Average Rating Over Time")
                    avg_rating = df.groupby('time_period')['overall'].mean().reset_index()
                    st.line_chart(avg_rating.set_index('time_period'))
                    
                with t_col2:
                    st.markdown("##### 💬 Sentiment Trend Over Time")
                    sentiment_trend = df.groupby(['time_period', 'sentiment']).size().unstack(fill_value=0)
                    st.line_chart(sentiment_trend)
            else:
                st.info("No 'reviewTime' column found in the dataset. Time-based trends are disabled.")
else:
    # Beautiful welcome page
    st.markdown("""
    <div class="info-card">
        <h3>Welcome to Sentilytics! 🚀</h3>
        <p>Sentilytics is a DevSecOps-enabled Sentiment Analysis platform. We classify customer reviews using Machine Learning (TF-IDF + Logistic Regression) and deep context-aware Transformer models (BERT).</p>
        <p><b>Getting Started:</b></p>
        <ul>
            <li>Please use the sidebar on the left to upload your customer review CSV file.</li>
            <li>Alternatively, toggle <b>"Use Sample Reviews Dataset"</b> in the sidebar to explore the analytics instantly with built-in review data.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=80", caption="Interactive Data Analytics", use_column_width=True)

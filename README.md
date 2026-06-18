# 🚀 Sentilytics

Sentilytics is an advanced sentiment analysis application utilizing dual Machine Learning models (TF-IDF + Logistic Regression and BERT) to achieve up to 93% classification accuracy. The app provides a fully interactive Streamlit dashboard for uploading, analyzing, visualizing, and exporting customer reviews, complete with robust DevSecOps, containerization, and Kubernetes configuration.

## 🔗 Live Demo

You can access the live dashboard here: **[sentilytics-devsecops.onrender.com](https://sentilytics-devsecops.onrender.com/)**

---

## 🌟 Key Features

- **Dual Sentiment Classification Engines**:
  - **Traditional ML**: TF-IDF vectorization paired with a Logistic Regression classifier (93% accuracy, fast, and lightweight).
  - **Deep Learning**: Fine-tuned multilingual BERT model (`nlptown/bert-base-multilingual-uncased-sentiment`) from Hugging Face Transformers for rich contextual understanding.
- **Interactive Analytics Dashboard**:
  - Direct file upload for custom review datasets in CSV format.
  - Live preview and real-time inference on the uploaded reviews.
  - Intuitive radio buttons to filter reviews dynamically by sentiment category (Positive, Neutral, Negative).
- **Rich Visualizations**:
  - Dynamic sentiment distribution bar charts.
  - Word Clouds generated separately for Positive and Negative reviews using cleaned tokenized text.
  - Temporal sentiment trend analysis (weekly, monthly, or daily granularity) mapping average star ratings and sentiment counts over time.
- **Misleading Reviews Detection**: Automatically flags reviews that have high ratings (e.g., 5-stars) but exhibit negative/neutral predicted sentiments.
- **Data Exporting**: Download annotated reviews containing predicted sentiments directly as a CSV.
- **Production-Ready DevSecOps Pipeline**:
  - Containerized deployment using Docker.
  - Multi-replica deployment configuration via Kubernetes.
  - Continuous Integration (CI) and automated image publishing via GitHub Actions.
  - Automated security vulnerability scanning using Trivy.

---

## 📁 Repository Structure

* [app.py](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/app.py) - Streamlit dashboard web interface.
* [Sentiment_Analysis.ipynb](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/Sentiment_Analysis.ipynb) - Jupyter Notebook showcasing model exploration, cleaning, and training.
* [requirement.txt](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/requirement.txt) - List of Python package dependencies.
* [Dockerfile](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/Dockerfile) - Instruction set for packaging Sentilytics as a Docker container.
* [docker-compose.yml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/docker-compose.yml) - Service orchestration config for local container development.
* [k8s/](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/k8s) - Directory containing Kubernetes manifests:
  * [deployment.yaml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/k8s/deployment.yaml) - Defines a 2-replica Deployment of the app.
  * [service.yaml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/k8s/service.yaml) - Exposes the app to network traffic using a NodePort Service.
* [.github/workflows/](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/.github/workflows) - Automated CI/CD pipelines:
  * [ci.yml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/.github/workflows/ci.yml) - Runs dependency installation and basic validation tests.
  * [docker-publish.yml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/.github/workflows/docker-publish.yml) - Builds the Docker image and pushes it to Docker Hub on merge to `main`.
* [docs/security/trivy-report.txt](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/docs/security/trivy-report.txt) - Security vulnerability assessment report generated via Trivy.
* `sentiment_model.pkl` & `tfidf_vectorizer.pkl` - Serialized traditional machine learning model artifacts.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Matplotlib, Seaborn, WordCloud
- **NLP & Deep Learning**: PyTorch, Hugging Face Transformers, NLTK
- **Machine Learning**: Scikit-Learn
- **DevOps & Infrastructure**: Docker, Docker Compose, Kubernetes (K8s)
- **CI/CD**: GitHub Actions

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed.

### Option 1: Running Locally (Bare Metal)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sentilytics.git
   cd sentilytics
   ```

2. **Install Python dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirement.txt
   ```

3. **Launch the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

---

### Option 2: Running with Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t sentilytics:latest .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 8501:8501 sentilytics:latest
   ```
   Open your browser and navigate to `http://localhost:8501`.

3. **Or run using Docker Compose**:
   ```bash
   docker-compose up
   ```

---

### Option 3: Deploying to Kubernetes

Deploy the application to your Kubernetes cluster (e.g. Minikube or cloud provider K8s) using the provided manifests:

1. **Apply the Deployment**:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```

2. **Apply the Service**:
   ```bash
   kubectl apply -f k8s/service.yaml
   ```

3. **Access the Application**:
   Find the NodePort URL using:
   ```bash
   minikube service sentilytics-service --url
   ```
   Or query the service:
   ```bash
   kubectl get svc sentilytics-service
   ```

---

## 🧪 Model Details

### 1. TF-IDF + Logistic Regression
* **Pros**: Extremely fast, offline inference, low memory usage.
* **Accuracy**: 93% on test dataset.
* **Best For**: Rapid analysis of huge datasets.

### 2. BERT (Base Multilingual Uncased)
* **Pros**: Captures nuanced semantics, supports multiple languages, higher contextual sensitivity.
* **Cons**: Compute-intensive, slow on CPU.
* **Best For**: Deep context-dependent review classification.

---

## ⚙️ CI/CD & Security (DevSecOps)

- **Continuous Integration ([ci.yml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/.github/workflows/ci.yml))**: Checks out code, sets up Python 3.10, installs dependencies, and runs basic verification tests.
- **Docker Publishing ([docker-publish.yml](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/.github/workflows/docker-publish.yml))**: Automatically publishes new builds to Docker Hub (`kairavipadhariya/sentilytics:latest`) when changes are pushed to `main`.
- **Security Scans**: Vulnerabilities are scanned using Trivy. The output report is logged in [trivy-report.txt](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/docs/security/trivy-report.txt).

---

## 📈 CSV Data Format

To analyze custom data, upload a CSV containing:
- `reviewText` (Required): Textual content of the review.
- `overall` (Optional): Star rating from 1 to 5 (used to map true sentiment and detect misleading ratings).
- `reviewTime` (Optional): Datetime field (used to display historical sentiment trends).

### Example:
| reviewText | overall | reviewTime |
| :--- | :---: | :--- |
| "Absolutely love the product, worth every penny!" | 5 | 2026-06-18 |
| "The customer service was awful and it broke on day one." | 1 | 2026-06-15 |

---

## 🖼️ Application Screenshots

Here are some visual insights and results generated by the Sentilytics application:

<img width="2457" height="1075" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/36bc37a7-965c-4a5e-b734-71443e2d9a19" />
<img width="1106" height="892" alt="Sentiment Distribution Plot" src="https://github.com/user-attachments/assets/5516b4e4-d805-4eec-905e-7fad6fa7a85b" />
<img width="1054" height="1192" alt="Positive Review WordCloud" src="https://github.com/user-attachments/assets/3b11584b-71e6-493d-a741-47704b13c664" />
<img width="1094" height="1245" alt="Negative Review WordCloud" src="https://github.com/user-attachments/assets/80d423ea-a049-4637-b762-ca8b9a68799a" />
<img width="1104" height="1237" alt="Misleading Reviews Flagging" src="https://github.com/user-attachments/assets/17de3041-4eaf-46f1-9356-6d4c334f96fb" />

---

## 🤝 Contributing

Contributions, bug reports, and pull requests are welcome! Feel free to raise issues for aspect-based sentiment features or UI optimizations.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](file:///Users/kairavipadhariya/Documents/Cloud/projects/sentilytics-original/LICENSE) for more details.

---

*Built with Python, Streamlit, and a lot of coffee ☕*

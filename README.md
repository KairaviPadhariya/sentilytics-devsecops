# 🚀 Sentilytics – DevSecOps Enabled Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-2088FF?logo=githubactions)
![Trivy](https://img.shields.io/badge/Security-Trivy-1904DA)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)
![License](https://img.shields.io/badge/License-MIT-green)

Sentilytics is a sentiment analysis application that combines Machine Learning with modern DevSecOps practices. The application provides an interactive Streamlit dashboard for analyzing customer reviews while demonstrating an end-to-end software delivery pipeline using Docker, GitHub Actions, Trivy, Docker Hub, and Render.

---

# 🔗 Live Demo

🌐 **Application:** https://sentilytics-devsecops.onrender.com/

📦 **Docker Hub:** https://hub.docker.com/r/kairavipadhariya/sentilytics

📂 **GitHub Repository:** https://github.com/KairaviPadhariya/sentilytics-devsecops

---

# ⭐ Project Highlights

- 🤖 Machine Learning based Sentiment Analysis
- 📊 Interactive Streamlit Dashboard
- 📈 Data Visualization & Word Clouds
- 🐳 Docker Containerization
- 🔄 Automated CI Pipeline using GitHub Actions
- 🔐 Security Scanning using Trivy
- 📦 Automatic Docker Image Publishing
- ☁️ Cloud Deployment on Render

---

# 🏗️ Project Architecture

```
                  User
                    │
                    ▼
           Streamlit Dashboard
                    │
                    ▼
         Sentiment Prediction Engine
                    │
        TF-IDF + Logistic Regression
                    │
                    ▼
            Prediction Results


Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    ├── Build Docker Image
    ├── Run Trivy Security Scan
    └── Push Docker Image
            │
            ▼
        Docker Hub
            │
            ▼
         Render Cloud
            │
            ▼
      Live Application
```

---

# 👨‍💻 My Contributions

The original sentiment analysis application has been enhanced by me with a complete DevSecOps workflow.

Enhancements include:

- Docker Containerization
- Docker Compose Support
- GitHub Actions CI Pipeline
- Trivy Security Scanning
- Automated Docker Hub Publishing
- Cloud Deployment on Render
- Improved Project Documentation
- Deployment Architecture

Note: This repository builds upon an existing sentiment analysis application. My primary contributions include Docker containerization, GitHub Actions CI/CD, Trivy security scanning, Docker Hub automation, Render deployment, and comprehensive project documentation.

---

# 🌟 Features

## 🤖 Machine Learning

- TF-IDF Vectorization
- Logistic Regression Classifier
- Up to **93% classification accuracy**

---

## 📊 Interactive Dashboard

- Upload CSV reviews
- Live sentiment prediction
- Filter Positive/Neutral/Negative reviews
- Export predictions

---

## 📈 Visual Analytics

- Sentiment Distribution Chart
- Positive Word Cloud
- Negative Word Cloud
- Sentiment Trend Analysis
- Misleading Review Detection

---

## 🔐 DevSecOps

- Dockerized Application
- GitHub Actions CI Pipeline
- Trivy Vulnerability Scanning
- Docker Hub Image Publishing
- Cloud Deployment on Render

---

# 📂 Repository Structure

```
Sentilytics
│
├── app.py
├── Sentiment_Analysis.ipynb
├── requirement.txt
├── Dockerfile
├── docker-compose.yml
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-publish.yml
│       └── trivy.yml
│
├── docs/
│   └── security/
│       └── trivy-report.txt
│
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
│
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-Learn |
| NLP | NLTK |
| Deep Learning | Hugging Face Transformers, PyTorch |
| Visualization | Matplotlib, Seaborn, WordCloud |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Security | Trivy |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/KairaviPadhariya/sentilytics-devsecops.git

cd sentilytics-devsecops
```

---

## Install Dependencies

```bash
pip install -r requirement.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Visit:

```
http://localhost:8501
```

---

# 🐳 Run with Docker

Build Image

```bash
docker build -t sentilytics:latest .
```

Run Container

```bash
docker run -p 8501:8501 sentilytics:latest
```

Visit:

```
http://localhost:8501
```

---

## Using Docker Compose

```bash
docker compose up
```

---

# ⚙️ CI/CD Pipeline

Every push to the **main** branch automatically:

- Checks out the source code
- Installs project dependencies
- Validates the project
- Performs security scanning using Trivy
- Builds Docker image
- Pushes Docker image to Docker Hub

---

# 🔐 Security

Security scanning is performed using **Trivy**.

The scan checks for:

- Vulnerable dependencies
- Misconfigurations
- Secrets
- Known CVEs

Generated reports are stored in:

```
docs/security/trivy-report.txt
```

---

# 📊 Model Information

## TF-IDF + Logistic Regression

Advantages:

- Fast inference
- Lightweight
- Low memory usage
- Suitable for production

Accuracy:

**93%**

---

## BERT

Model:

```
nlptown/bert-base-multilingual-uncased-sentiment
```

Advantages:

- Context-aware prediction
- Multilingual support
- Better semantic understanding

Trade-offs:

- Slower than Logistic Regression
- Higher memory usage

---

# 📁 Dataset Format

The uploaded CSV should contain:

| Column | Required |
|----------|----------|
| reviewText | ✅ |
| overall | Optional |
| reviewTime | Optional |

Example

| reviewText | overall | reviewTime |
|------------|----------|------------|
| Great Product | 5 | 2026-06-18 |
| Bad Quality | 1 | 2026-06-15 |

---

# 📷 Application Screenshots

## Dashboard

(Add Screenshot)

## Sentiment Distribution

(Add Screenshot)

## Positive Word Cloud

(Add Screenshot)

## Negative Word Cloud

(Add Screenshot)

## Misleading Review Detection

(Add Screenshot)

---

# 📚 What I Learned

This project helped me gain practical experience in:

- Machine Learning Deployment
- Docker Containerization
- GitHub Actions
- Continuous Integration
- DevSecOps Fundamentals
- Container Security
- Docker Hub Automation
- Cloud Deployment
- Software Documentation

---

# 🚀 Future Improvements

- Unit Testing using Pytest
- Code Quality Checks using Black & Flake8
- Improved ML Model Performance
- Authentication for Dashboard
- Monitoring & Logging
- Kubernetes Deployment (planned as a future learning milestone)

---

# 🤝 Contributing

Contributions, suggestions, and pull requests are welcome.

Feel free to open an issue for bug reports or feature requests.

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a Star!

Built with ❤️ using Python, Streamlit, Docker, GitHub Actions, Trivy, and Render.
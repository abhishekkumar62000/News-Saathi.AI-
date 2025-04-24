
![19 04 2025_17 13 50_REC](https://github.com/user-attachments/assets/a3e3459d-5ae9-472a-b212-c6620ad0a66f)
![19 04 2025_17 13 16_REC](https://github.com/user-attachments/assets/782813ba-292a-4bd2-9176-3f78e6c8d903)


---

# 🤖 News Saathi.AI 🌐🔍  
### *AI‑Driven Breaking News Platform*  
📍 **Live App**: [https://news-saathi-ai.streamlit.app](https://news-saathi-ai.streamlit.app)

---

## 📌 Overview

**News Saathi.AI** is a cutting-edge **Streamlit-based web application** that blends **AI intelligence**, **API integrations**, and **visual tools** to help users **generate blog posts**, **analyze trending news**, and **summarize articles** with ease.

Whether you’re a **blogger**, **researcher**, or **casual reader**, this platform offers everything you need to create or consume high-quality news content, powered by **NLP models** and **real-time news APIs**.

---

## 🛠 Features

### 🧠 1. AI News Generator
- 📚 Input any topic or choose from suggestions.
- ✍️ Auto-generate **long-form blog posts**.
- 🎛 Customize:
  - **Temperature** (creativity)
  - **Tone** (Formal, Neutral, Informal)
  - **Language**: English, Hindi, Maithili, Bhojpuri
- 🤖 **AI Agents**:
  - 🕵️‍♂️ *Senior Research Analyst* – Deep research on the topic
  - ✍️ *Content Writer* – Crafts content from research
- 📝 **Downloadable Markdown** files.

---

### 📰 2. Top 10 Indian Newspapers
- 📌 Curated list of India's most popular newspapers
- 🖼 Logos for quick recognition
- 🔗 Direct website links (e.g., TOI, HT, The Hindu)

---

### 📈 3. Trending News Analysis
- 🔍 Fetch latest headlines (via NewsAPI)
- 😊 Sentiment Analysis: Positive / Neutral / Negative
- 📊 Bar chart visualizations
- ☁️ Word Cloud of trending topics
- 📰 Top 5 clickable articles with title, description & links

---

### ✂️ 4. AI News Summarizer
- 📄 Paste a news article or provide a URL
- 🧾 Generate **Short**, **Medium**, or **Detailed** summaries
- 📥 Download as `.txt` file

---

### 🖼 5. Relevant Image Suggestions
- 🔗 Pulls images from Unsplash
- 🖼 Top 3 matched images with captions displayed

---

### ⭐ 6. User Feedback
- ⭐ Rate output (1 to 5 stars)
- 💬 Submit detailed feedback
- 📈 Helps improve future iterations

---

### 📲 7. Social Media Integration
- 🐦 Share content on Twitter, LinkedIn, WhatsApp, and Facebook
- 📝 Pre-written captions for easy sharing

---

### 👨‍💻 8. Developer Credits
- 🧑‍💻 Developed by **Abhishek Yadav**
- 🖼 Profile picture + name shown in sidebar
- 🎨 Custom News Saathi.AI branding

---

### 🧭 9. Responsive Design
- 🧩 Streamlit Tabs for feature organization
- 🌙 Dark Mode toggle

---

### ⚠️ 10. Robust Error Handling
- 🧾 Friendly messages for API/key issues
- 🐞 Error logs for debugging

---

## ⚙️ Technologies Used

- **Languages**: Python 🐍
- **Framework**: Streamlit 🎈
- **AI Model**: Cohere’s Command-R 🤖
- **APIs**:
  - NewsAPI 🗞
  - Unsplash API 🖼
  - Serper API 🔍
- **Libraries**:
  - `dotenv` – for environment variables
  - `requests` – for API calls
  - `nltk` – for NLP tasks
  - `wordcloud`, `matplotlib` – for visualizations
  - `newspaper3k` – for article parsing and summarizing

---

## 🧰 Project Setup Guide

> 🚨 Make sure you have Python 3.8+ installed on your system

### 🪛 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/news-saathi-ai.git
cd news-saathi-ai
```

### 📦 Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 📥 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔐 Step 4: Set Up Environment Variables
Create a `.env` file in the root directory and add your API keys:

```
NEWS_API_KEY=your_newsapi_key
UNSPLASH_ACCESS_KEY=your_unsplash_key
SERPER_API_KEY=your_serper_key
COHERE_API_KEY=your_cohere_key
```

### ▶️ Step 5: Run the App
```bash
streamlit run app.py
```

> 🎉 Your app will run locally at `http://localhost:8501`

---

## 📊 How It Works

1. **User Input**: Enter topic or article URL
2. **AI Agent**: Researches topic using APIs and LLMs
3. **Content Generator**: Crafts and displays content
4. **Enhancer**: Adds images, sentiment, and summaries
5. **Output Delivery**: Results shown with download/share options

---

## ✅ Live Demo

🟢 Try it here: [https://news-saathi-ai.streamlit.app](https://news-saathi-ai.streamlit.app)

---

## 🤝 Contributing

Got ideas? Found a bug? Want to collaborate?

1. Fork the repo 🍴
2. Create a branch (`git checkout -b feature-X`)
3. Commit changes (`git commit -m 'Add feature X'`)
4. Push (`git push origin feature-X`)
5. Create Pull Request ✅

---

## 🙏 Acknowledgements

Thanks to:
- [Streamlit](https://streamlit.io/)
- [Cohere](https://cohere.com/)
- [NewsAPI](https://newsapi.org/)
- [Unsplash Developers](https://unsplash.com/developers)
- [Serper API](https://serper.dev/)

---

## 🧑‍💻 Developer

**👨‍💻 Abhishek Yadav**  
Passionate about AI, news tech, and simplifying information access for the world.

---

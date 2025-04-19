# 🤖 AI-Powered Social Media Auto-Tagging System

An intelligent local system that automatically generates smart hashtags from **text** and **images**, and redirects users to post on **Twitter** or **LinkedIn** seamlessly. Ideal for content creators, marketers, or automation enthusiasts. Built with **Python**, **Flask**, and **transformers**.

---

## 🚀 Project Overview

This AI system allows a user to:

- ✍️ **Write text** (a post, caption, or message)
- 📷 **Upload an image** (optional)
- ✨ **Automatically generate relevant tags** using AI models
- 💬 **Redirect to Twitter/LinkedIn** with content pre-filled (no login required to this app)

---

## 🔧 Tech Stack

| Layer        | Technology Used                            |
| ------------ | ------------------------------------------ |
| Frontend     | HTML, CSS, JS (via Flask templates)        |
| Backend      | Flask (Python)                             |
| AI (Text)    | KeyBERT (MiniLM Transformer)               |
| AI (Image)   | Hugging Face `image-classification` model  |
| Posting Flow | Twitter Intent URL, LinkedIn Share URL     |
| Deployment   | Docker-ready (runs locally in a container) |

---

## 🧰 System Architecture

```
+--------------+        +--------------+        +----------------+        +----------------------+
|  User Input  | -----> | Flask Server | -----> | AI Tagging Core| -----> | Social Platform Page |
| (Text/Image) |        | (app.py)     |        | (Text + Image) |        | (via Redirect URL)   |
+--------------+        +--------------+        +----------------+        +----------------------+
```

---

## 📅 Features

- [x] Local keyword extraction from text using **KeyBERT**
- [x] Smart label detection from images using **Vision Transformers**
- [x] Combines both to produce up to 5 relevant **#hashtags**
- [x] Sends the user to **Twitter** or **LinkedIn** for final posting
- [x] Works **offline/local** with zero external API dependencies

---

## ⚡ Quick Start

```bash
git clone https://github.com/your-username/ai-tagging-system.git
cd ai-tagging-system
python3 -m venv venv
source venv/bin/activate       # or venv\Scripts\activate.bat (Windows)
pip install -r requirements.txt
flask run
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🔹 How to Use

1. Write a short post or caption in the text area
2. Upload an image (optional)
3. Click **Generate Tags**
4. Review the auto-generated hashtags
5. Choose your platform (Twitter/LinkedIn)
6. Click **Post Now** to be redirected to post with prefilled content

---

## 🔍 AI Models Used

### ✏️ Text Tagging

- **KeyBERT** with `all-MiniLM-L6-v2`
- Extracts meaningful keyphrases and converts them to hashtags

### 📸 Image Tagging

- Hugging Face **`pipeline("image-classification")`**
- Detects top objects from uploaded image and returns confidence scores

---

## 📄 Sample Output

Given:

```
Text: Exploring AI in healthcare
Image: doctor-with-tablet.jpg
```

You get:

```
#Healthcare #AIinMedicine #Doctor #Tablet #Innovation
```

---

## 🚧 Future Work

- ☁️ Switch to OpenAI or AWS Rekognition in cloud mode
- 📁 Add local SQLite / DynamoDB history
- 🤖 Use Retrieval-Augmented Generation (RAG) for personalized tags
- 🛋️ Add support for Instagram and Facebook posting

---

## 🚧 Docker Support

```bash
docker build -t ai-tagger .
docker run -p 5000:5000 ai-tagger
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🙏 Credits

Made with ❤️ by a passionate graduate student exploring the intersection of **AI** and **practical applications**.

- Email: your.email@example.com
- GitHub: [your-username](https://github.com/your-username)

---

## 🚩 License

MIT License. Feel free to fork, extend, and contribute!

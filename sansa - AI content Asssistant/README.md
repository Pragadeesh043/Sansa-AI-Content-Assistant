
# 🧠 Sansa – AI Content Assistant for Educators

**Sansa** is a user-friendly, conversational AI assistant built for educators. It helps teachers generate educational and professional content effortlessly by combining the power of modern language models with an intuitive Streamlit interface.

---

## ✨ Features

- ✏️ Generate content like blog intros, article summaries, social media captions, emails, and more
- ⚙️ Choose from powerful LLMs (LLaMA3, DeepSeek)
- 💬 Chat-style interface for a natural, intuitive experience
- 🗂️ Session history maintained during conversation
- 🔐 Secure API key input via sidebar
- 🚀 Fast and responsive using Groq's infrastructure

---

## 🎯 Project Objectives

- Develop a functional AI assistant tailored to educational content needs
- Make LLMs accessible to non-technical users like teachers
- Integrate Streamlit, Langchain, and Groq APIs in a practical tool
- Evaluate AI-generated content for coherence, relevance, and usefulness

---

## 🧱 Tech Stack

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Langchain](https://www.langchain.com/)
- [Groq LLM API](https://groq.com/)
- `dotenv` for environment variable management

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Pragadeesh043/Sansa-AI-Content-Assistant.git
cd Sansa-AI-Content-Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## 🔐 Authentication

- Enter your **Groq API key** in the sidebar
- The key is securely input using a password field and is not stored or logged

---

## 🖥️ User Interface

- **Chat interface** where messages from user and AI are styled differently
- **Sidebar** for model selection and API key input
- **Clear chat** button to reset the conversation

---

## 💡 Example Use Cases

### Blog Intro Prompt

> "Write an engaging intro for a blog on mindfulness in education"

**Response:**
> “Mindfulness is transforming classrooms across the globe…”

---

### Social Media Caption

> "Create a catchy caption for a school’s Earth Day event"

**Response:**
> “🌍 Let’s make every day Earth Day! Join us…”

---

### Article Summary

> "Summarize an article on the impact of technology on student engagement"

**Response:**
> “Technology has revolutionized student engagement by providing…”

---

## ⚠️ Limitations

- Requires a valid API key for each session
- Dependent on internet access and Groq's API availability
- Long chat histories are truncated to the latest 100 messages
- Some responses may require human editing due to hallucinations or bias

---

## 🛡️ Security

- API keys are not stored or exposed
- Inputs use secure Streamlit password fields
- App handles failures with user-friendly messages

---

## 📁 Folder Structure

```
Sansa-AI-Content-Assistant/
├── app.py
├── requirements.txt
├── README.md
└── .env (optional)
```

---

## 📃 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 👤 Author

Developed by **Pragadeesh**  
🔗 [GitHub Profile](https://github.com/Pragadeesh043)

---

## 🙌 Acknowledgements

- OpenAI / Meta / DeepSeek for LLMs
- Groq for blazing-fast inference
- Langchain for model orchestration
- Streamlit for UI simplicity

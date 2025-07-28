# 🤖 AI Chatbot using Gemini Flash 2.0 + Streamlit

This project is a simple yet powerful chatbot built using **Gemini Flash 2.0**, Google’s lightweight, high-speed language model, and served via **Streamlit**, a Python-based web framework for rapid prototyping. The chatbot runs locally and supports real-time interaction with an LLM through your browser.

---

## ✨ Features

- 🔮 **Gemini Flash 2.0** — fast, cost-efficient model for quick responses
- 🌐 **Streamlit CLI** — turns your Python script into a web app with one command
- 🔐 API key secured using `.env` file
- 🧩 Lightweight and easy to extend

---

## 🧱 Tech Stack

- **Frontend & Interface**: [Streamlit](https://streamlit.io/)
- **LLM Backend**: [Google Gemini Flash 2.0](https://ai.google.dev/)
- **Environment Handling**: `python-dotenv`

---

## 🚀 Getting Started

Follow these steps to set up and run the chatbot on your machine.

---

### 🔧 Step 1: Clone the Repository

```powershell
git clone https://github.com/SamayraS/AIchatbot.git
cd AIchatbot
```

### ✅ Step 2: Set Up Python Environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 🔧 Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

### 🔐🟢 Steps 4 & 5: Add API Key and Run the App

1. Create a `.env` file in the root directory and add your Gemini API key:

    ```
    GEMINI_API_KEY=your-api-key-here
    ```

    > 💡 You can get your API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

2. Start the chatbot app using Streamlit:

    ```powershell
    streamlit run app.py
    ```

    > 🟢 The app will open in your default browser at [http://localhost:8501](http://localhost:8501)

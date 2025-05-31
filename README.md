# LLM Powered QA Chatbot

An LLM Powered Question Answering chatbot application built with Python, UV, and Chainlit.


## Getting Started

### 1️⃣ Install UV

First, install **UV** (if not already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```sh
uv --version
```

---

### 2️⃣ Create and Initialize the Project

```sh
uv init qa-chatbot
cd qa-chatbot
```

---

### 3️⃣ Install Chainlit (Dependency)

```sh
uv add chainlit google-generativeai python-dotenv
```

---

### 4️⃣ Activate UV Virtual Environment 

For Windows:

```sh
.venv\Scripts\activate
```

For Linux/macOS:

```sh
source .venv/bin/activate
```

---

### 5️⃣ Create .env file

Create a `.env` file in the root directory of the project and add the following:

```sh
GEMINI_API_KEY=your_gemini_api_key
```

Get Google Gemini API key from [here](https://aistudio.google.com/app/apikey)

---

### 6️⃣ Run QA Chatbot (Web App)

```sh
chainlit run main.py -w
```

Go to the following URL:

```sh
http://localhost:8000
```

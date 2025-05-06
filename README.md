
# 📊 Financial Data Extractor using LangChain + Groq

This project is a simple Streamlit-based web application that leverages **LangChain**, **Groq's LLM**, and **Prompt Engineering** to extract structured financial data—**Revenue (Actual & Expected)** and **EPS (Actual & Expected)**—from unstructured news articles or financial paragraphs.

---

## 📁 Project Structure

```
.
├── data_extractor.py   # Handles prompt creation and LLM-based data extraction
├── main.py             # Streamlit app for user interaction
├── .env                # Environment variables (API keys, etc.)
```

---

## 🔧 Requirements

Install the dependencies:

```bash
pip install streamlit pandas python-dotenv langchain langchain-groq
```

Ensure you have a `.env` file containing the necessary environment variables for Groq, such as:

```
GROQ_API_KEY=your_groq_api_key
```

---

## 🚀 How It Works

1. **User Input**: User enters a financial news paragraph.
2. **Prompting**: `data_extractor.py` creates a prompt and passes it to Groq's LLM using LangChain.
3. **Extraction**: The model returns a structured JSON with actual and expected revenue and EPS.
4. **Display**: The extracted data is formatted and shown in a table in the Streamlit app.

---

## 📦 Files Overview

### `data_extractor.py`

- Initializes the Groq LLM with LangChain.
- Constructs a prompt asking the LLM to extract financial data in JSON.
- Parses the LLM's response into a structured Python dictionary.

### `main.py`

- Builds a Streamlit interface.
- Allows users to paste financial text.
- Displays a nicely formatted output table using pandas and Streamlit.

---

## 🧪 Example

Input:
```
Company X reported a revenue of $5.4 billion beating the expected $5.0 billion. EPS came in at $1.20, slightly above the expected $1.15.
```

Output Table:

| Measure | Estimated | Actual   |
|---------|-----------|----------|
| Revenue | $5.0B     | $5.4B    |
| EPS     | $1.15     | $1.20    |

---

## ✅ Features

- Uses **LangChain** with **Groq's LLM**.
- Automatic **JSON parsing** for clean outputs.
- Built with **Streamlit** for easy UI.
- Robust error handling for malformed outputs.

---

## 📌 Notes

- Be sure to run `load_dotenv()` before accessing environment variables.
- The model used: `llama-3.3-70b-versatile`.

---

## ▶️ Run the App

```bash
streamlit run main.py
```

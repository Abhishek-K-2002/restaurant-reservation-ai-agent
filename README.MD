# 🍽️ FoodieSpot AI Reservation Agent

A conversational AI agent built for **restaurant reservation & recommendation** using **Gemini 1.5 Flash API** + **Streamlit**, implementing tool calling architecture **without LangChain**.

---

## 🛠 Features
- Intent detection (recommend, book, fallback) via Gemini LLM.
- Simple, clean Streamlit UI.
- No hardcoded logic — flow driven by LLM.
- Uses JSON restaurant data (`restaurants_data.json`).
- Separated tools and logic for modularity.

---

## 🚀 How to Run

1. Install requirements:
```bash
pip install streamlit google-generativeai

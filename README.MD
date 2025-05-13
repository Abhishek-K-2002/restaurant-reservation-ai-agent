**FoodieSpot AI Reservation Agent**

A conversational AI agent built for **restaurant reservation and recommendation** using **Google Gemini 1.5 Flash API** + **Streamlit**, implementing a **proper tool calling architecture without LangChain or any other frameworks**.

---

**Features**

-  **LLM-driven Intent Detection**:  
  Uses Gemini 1.5 Flash to classify user intent into:
  - `recommend_restaurant`
  - `book_table`
  - `greeting`
  - `fallback`

-  **No hardcoded logic**:
  - No manual keyword checks like `if 'book' in user_input`.
  - All decisions are made by the **LLM's JSON response**.
  
-  **Proper Tool Calling Pattern**:
  - Based on the returned intent, the system calls the corresponding tool (function) dynamically.
  
-  **Simple Streamlit UI**:
  - Clean interface to interact with the agent.
  - Supports text input, displays dynamic UI elements depending on the user intent.
  
-  **Modular Design**:
  - Tools like recommending restaurants, booking tables, or greeting are separated into `tools.py`.
  - Business logic is cleanly separated from UI and LLM client code.
  
-  **Uses JSON data**:
  - Sample data is provided in `restaurants_data.json`.

---

##  How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/restaurant_ai_agent.git
cd restaurant_ai_agent

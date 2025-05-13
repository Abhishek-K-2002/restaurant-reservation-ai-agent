import streamlit as st
from llm_client import call_llm_api
from tools import load_restaurants, recommend_restaurant_ui, book_table_ui, handle_greeting
import json

st.title("FoodieSpot Reservation AI Assistant")

restaurants = load_restaurants()

user_input = st.text_input("Ask me to recommend or book a table...")

if user_input:
    llm_response = call_llm_api(user_input)
    try:
        llm_response_json = json.loads(llm_response)
        intent = llm_response_json['intent']
    except Exception as e:
        st.error(f"LLM returned invalid response: {llm_response}")
        st.warning("Sorry, I didn't understand that. Please try again.")
        st.stop()


    if intent == "recommend_restaurant":
        recommend_restaurant_ui(restaurants, st)
    elif intent == "book_table":
        book_table_ui(restaurants, st)
    elif intent == "greeting":
        st.write(handle_greeting(user_input))
    else:
        st.warning("Sorry, I didn't understand that. Please try again.")

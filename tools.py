import json

def load_restaurants(file_path="restaurants_data.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def recommend_restaurant_ui(restaurants, st):
    st.subheader("Recommended Restaurants")
    for r in restaurants:
        st.write(f"- {r['name']} ({r['cuisine']}, Seats: {r['capacity']})")

def handle_greeting(user_input):
    return "👋 Hello! How can I assist you with your dining plans today?"


def book_table_ui(restaurants, st):
    st.subheader("Book a Table")
    name = st.text_input("Enter your name")
    selected_restaurant = st.selectbox("Choose Restaurant", [r['name'] for r in restaurants])
    guests = st.number_input("Number of guests", min_value=1, max_value=20, value=2)
    if st.button("Book Now"):
        st.success(f"✅ Table for {guests} booked at {selected_restaurant}. Thank you, {name}!")

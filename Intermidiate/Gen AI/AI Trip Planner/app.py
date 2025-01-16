import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key='AIzaSyA_uyoC2xL9CG1YyqU_12kEiP5X6JbiGpc')

#Model For Generating
model = genai.GenerativeModel('gemini-pro')

# Function for trip planning
def generate_trip_plan(duration, destination, style, budget):
    prompt = (f"Create a {duration}-day trip itinerary for {destination} focusing on {style} travel. "
              f"Include daily activities, must-see attractions, and accommodation suggestions within a budget of Rs {budget}.")
    try:
        response = model.generate_content(prompt) 
        return response.text.strip()
    except Exception as e:
        return f"Error generating trip plan: {e}"

# Streamlit app
st.set_page_config(page_title="AI Trip Planner", layout="centered")

st.title("🌍 AI Trip Planner by Tejas")
st.markdown("Plan your perfect trip with the power of AI! Enter your preferences below to get a personalized itinerary.")

# User inputs
duration = st.number_input("Trip Duration (days)", min_value=1, step=1, help="How many days will your trip last?")
destination = st.text_input("Trip Destination", help="Where would you like to travel?")

# Trip style selection
style_options = ["Adventure", "Relaxation", "Cultural", "Other"]
style = st.selectbox("Trip Style", style_options, help="Select your preferred travel style. Choose 'Other' to specify your own.")

if style == "Other":
    custom_style = st.text_input("Enter your own travel style", help="Describe your preferred travel style in your own words.")
    if custom_style.strip():
        style = custom_style  # Use the custom input as the style
    else:
        style = "Custom"  # Placeholder if the user doesn't enter anything

budget = st.number_input("Total Budget (Rs)", min_value=5000, step=1000, help="Enter your estimated trip budget.")

# Generate trip plan
if st.button("Generate Trip Plan"):
    if destination.strip():
        with st.spinner("Generating your trip plan..."):
            trip_plan = generate_trip_plan(duration, destination, style, budget)
        st.subheader("Your Trip Plan:")
        st.write(trip_plan)
    else:
        st.error("Please enter a valid trip destination.")

import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyD7zjs9xk8pgyZD6MzGAYC1G2FIxh2Np0s")

# Model For Generating
model = genai.GenerativeModel('gemini-pro')

# Function To Generate  Savings PLan
def generate_savings_plan(income,fixed_expenses,variable_expenses,goal,duration):

    prompt = (f"create a monthly savings plan. My monthly income is {income} INR. "
              f"My fixed expenses are {fixed_expenses} INR, and my variable expenses are {variable_expenses} INR. "
              f"I want to save {goal} INR in {duration} months. Provide a breakdown of how much I should save each month "
              "and suggest adjustments to my budget if necessary.")  
    response = model.generate_content(prompt)
    return response.text

# Streamlit app 
st.set_page_config(page_title="Personalized Savings Plan Generator", layout="centered")
st.title("Personalized Savings Plan Generator")
st.subheader("Plan your savings effortlessly!")

# User inputs
income = st.number_input("Enter your monthly income (in INR):", min_value=0, step=1000)
fixed_expenses = st.number_input("Enter your fixed monthly expenses (in INR):", min_value=0, step=500)
variable_expenses = st.number_input("Enter your variable monthly expenses (in INR):", min_value=0, step=500)
goal = st.number_input("Enter your savings goal (in INR):", min_value=0, step=1000)
duration = st.number_input("Time to achieve goal (in months):", min_value=1, step=1)

#Button to Generate Savings Plan
submit = st.button("Generate Savings Plan")
if submit:
    if income > 0 and fixed_expenses >= 0 and variable_expenses >= 0 and goal > 0 and duration > 0:
        with st.spinner("Generating your Savings Plan..."):
            savings_plan = generate_savings_plan(income, fixed_expenses, variable_expenses, goal, duration)
        st.subheader("Your Savings Plan")
        st.write(savings_plan)
    else:
        st.warning("Please fill all the fields correctly to generate your savings plan.")
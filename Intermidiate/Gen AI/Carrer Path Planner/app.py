import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key='AIzaSyD7zjs9xk8pgyZD6MzGAYC1G2FIxh2Np0s')

# Model For Generating
model = genai.GenerativeModel('gemini-pro')

# Function To Generate  Carrer Roadmap
def generate_carrer_roadmap(skills,goal,duration):

    prompt = (f"Given the skills {skills}, suggest a career roadmap to achieve the goal of {goal} within {duration} months." 
              f"Provide an overview, include key skills that are important for {goal}, job roles, and suggested milestones.")  
    response = model.generate_content(prompt)
    return response.text

# Streamlit app
st.set_page_config(page_title="Carrer Path Planner", layout="centered")
st.title("Carrer Path Planner By Tejas")
st.markdown("Create your Personalized Carrer Path Plan using the power of AI to achieve your Goal.")

# User Inputs 
current_role = st.text_input("Current Job Role")
skills = st.text_area("Skills (comma-seperated)")
carrer_goal = st.text_input("Desired Carrer Goal")
duration = st.number_input("Goal Achievement Time (months)", min_value=1, step=1)
# Button to Generate Carrer Roadmap
submit = st.button("Generate Carrer Path")
if submit:
    if current_role and skills and carrer_goal:
        with st.spinner("Generating your Carrer Roadmap..."):
            roadmap = generate_carrer_roadmap(skills,carrer_goal,duration)
        st.subheader("Your Carrer Roadmap")
        st.write(roadmap)
    else:
        st.warning("Please provide all Inputs Properly!!!!")
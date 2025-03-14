import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

def generate_custom_resume(name, email, phone, education, experience, skills, job_description):
    prompt = f"""
    Generate a structured resume in plain text format.
    
    Name: {name}
    Email: {email}
    Phone: {phone}
    
    **Education:**
    {education}
    
    **Experience:**
    {experience}
    
    **Skills:**
    {skills}
    
    Tailor this resume to the following job description:
    {job_description}
    """
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("SmartResume Generator")
    st.write("Generate a customized resume tailored to a job description.")
    
    with st.form("resume_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        education = st.text_area("Education")
        experience = st.text_area("Work Experience")
        skills = st.text_area("Skills")
        job_description = st.text_area("Job Description")
        
        submitted = st.form_submit_button("Generate Resume")
    
    if submitted:
        if not all([name, email, phone, education, experience, skills, job_description]):
            st.error("Please fill in all fields.")
        else:
            resume_content = generate_custom_resume(name, email, phone, education, experience, skills, job_description)
            st.success("Resume Generated Successfully!")
            st.text_area("Your Resume:", resume_content, height=300)

if __name__ == "__main__":
    main()

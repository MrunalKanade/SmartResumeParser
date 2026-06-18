import streamlit as st
import pandas as pd

from parser.pdf_parser import extract_text_from_pdf

from parser.extractor import (
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience
)

from parser.scorer import calculate_score


st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    data = {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }

    score = calculate_score(data)

    st.subheader("Extracted Information")

    st.write("### Email")
    st.write(data["email"])

    st.write("### Phone")
    st.write(data["phone"])

    st.write("### Skills")
    st.write(data["skills"])

    st.write("### Education")
    st.write(data["education"])

    st.write("### Experience")
    st.write(data["experience"])

    st.metric(
        label="Resume Score",
        value=f"{score}/100"
    )

    df = pd.DataFrame([data])

    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="resume_data.csv",
        mime="text/csv"
    )

    st.download_button(
        label="Download JSON",
        data=df.to_json(
            orient="records",
            indent=4
        ),
        file_name="resume_data.json",
        mime="application/json"
    )
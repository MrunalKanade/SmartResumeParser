import streamlit as st
import pandas as pd

from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx

from parser.extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github,
    extract_skills,
    extract_education,
    extract_experience
)

from parser.scorer import calculate_score


# Page Configuration
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Resume Parser")
st.write("Upload one or multiple resumes and extract information.")

# Multiple Upload
uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

all_data = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        # PDF
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)

        # DOCX
        elif uploaded_file.name.endswith(".docx"):
            text = extract_text_from_docx(uploaded_file)

        else:
            continue

        # Extract Information
        data = {

            "name": extract_name(text),

            "email": extract_email(text),

            "phone": extract_phone(text),

            "linkedin": extract_linkedin(text),

            "github": extract_github(text),

            "skills": extract_skills(text),

            "education": extract_education(text),

            "experience": extract_experience(text)

        }

        # Resume Score
        score = calculate_score(data)

        data["resume_score"] = score

        all_data.append(data)

        # Display Individual Resume
        st.divider()

        st.subheader(uploaded_file.name)

        st.write("### Name")
        st.write(data["name"])

        st.write("### Email")
        st.write(data["email"])

        st.write("### Phone")
        st.write(data["phone"])

        st.write("### LinkedIn")
        st.write(data["linkedin"])

        st.write("### GitHub")
        st.write(data["github"])

        st.write("### Skills")
        st.write(data["skills"])

        st.write("### Education")
        st.write(data["education"])

        st.write("### Experience")
        st.write(data["experience"])

        st.metric(
            "Resume Score",
            f"{score}/100"
        )

# Summary Table
if len(all_data) > 0:

    st.divider()

    st.subheader("Summary Table")

    df = pd.DataFrame(all_data)

    st.dataframe(df)
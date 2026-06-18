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


# Page Config
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Resume Parser")

st.write("Upload one or more resumes and analyze them.")

# Required Skills
required_skills_input = st.text_input(
    "Enter Required Skills (comma separated)",
    placeholder="Python, SQL, Machine Learning"
)

required_skills = [
    skill.strip()
    for skill in required_skills_input.split(",")
    if skill.strip()
]

# Upload files
uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

all_data = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        # Extract text
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)

        elif uploaded_file.name.endswith(".docx"):
            text = extract_text_from_docx(uploaded_file)

        else:
            continue

        # Extract information
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

        # Score
        score = calculate_score(data)

        data["resume_score"] = score

        # Skill Matching
        matched_skills = list(
            set(required_skills).intersection(
                set(data["skills"])
            )
        )

        if len(required_skills) > 0:

            match_percentage = round(
                len(matched_skills) /
                len(required_skills) * 100,
                2
            )

        else:

            match_percentage = 0

        data["matched_skills"] = matched_skills
        data["match_percentage"] = match_percentage

        all_data.append(data)

        # Individual Resume Display
        st.divider()

        st.subheader(uploaded_file.name)

        col1, col2 = st.columns(2)

        with col1:

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

        with col2:

            st.write("### Skills")
            st.write(data["skills"])

            st.write("### Education")
            st.write(data["education"])

            st.write("### Experience")
            st.write(f"{data['experience']} years")

            st.write("### Matched Skills")
            st.write(matched_skills)

        st.metric(
            "Resume Score",
            f"{score}/100"
        )

        st.metric(
            "Skill Match %",
            f"{match_percentage}%"
        )

# Summary Table
if len(all_data) > 0:

    st.divider()

    st.subheader("Summary Table")

    df = pd.DataFrame(all_data)

    st.dataframe(df)

    # Candidate Ranking
    st.divider()

    st.subheader("🏆 Candidate Ranking")

    ranked_df = df.sort_values(
        by=["match_percentage", "resume_score"],
        ascending=False
    )

    st.dataframe(
        ranked_df[
            [
                "name",
                "email",
                "resume_score",
                "match_percentage"
            ]
        ]
    )

    # Save Output Files
    df.to_csv(
        "outputs/resume_data.csv",
        index=False
    )

    df.to_json(
        "outputs/resume_data.json",
        orient="records",
        indent=4
    )

    # Download CSV
    st.download_button(
        label="⬇ Download CSV",
        data=df.to_csv(index=False),
        file_name="resume_data.csv",
        mime="text/csv"
    )

    # Download JSON
    st.download_button(
        label="⬇ Download JSON",
        data=df.to_json(
            orient="records",
            indent=4
        ),
        file_name="resume_data.json",
        mime="application/json"
    )
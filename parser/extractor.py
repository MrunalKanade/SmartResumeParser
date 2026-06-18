import re
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

skills_df = pd.read_csv("data/skills.csv")

SKILLS = skills_df["skills"].tolist()


def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":

            return ent.text

    return "Not Found"


def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    emails = re.findall(pattern, text)

    return emails[0] if emails else "Not Found"


def extract_phone(text):

    pattern = r'(\+91[\-\s]?)?[6-9]\d{9}'

    phones = re.findall(pattern, text)

    return phones[0] if phones else "Not Found"


def extract_linkedin(text):

    pattern = r'linkedin\.com/in/\S+'

    links = re.findall(pattern, text)

    return links[0] if links else "Not Found"


def extract_github(text):

    pattern = r'github\.com/\S+'

    links = re.findall(pattern, text)

    return links[0] if links else "Not Found"


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return list(set(found_skills))


def extract_education(text):

    education_keywords = [
        "Bachelor",
        "Master",
        "B.Tech",
        "M.Tech",
        "MBA",
        "BCA",
        "MCA",
        "Degree",
        "B.E",
        "M.E",
        "BSc",
        "MSc",
        "PhD"
    ]

    education = []

    for keyword in education_keywords:

        if keyword.lower() in text.lower():

            education.append(keyword)

    return education


def extract_experience(text):

    pattern = r'(\d+)\+?\s+years'

    matches = re.findall(pattern, text)

    if matches:

        return max(matches)

    return "0"
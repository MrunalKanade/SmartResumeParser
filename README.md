\# 📄 Smart Resume Parser



A Python-based Resume Parser that extracts structured information from PDF and DOCX resumes using regex, keyword matching, and NLP techniques. The application provides candidate details, resume scoring, skill matching, ranking, and export functionality through an interactive Streamlit interface.



\---



\## 🚀 Features



\- ✅ PDF Resume Parsing

\- ✅ DOCX Resume Parsing

\- ✅ Multiple Resume Upload

\- ✅ Name Extraction

\- ✅ Email Extraction

\- ✅ Phone Number Extraction

\- ✅ LinkedIn Profile Extraction

\- ✅ GitHub Profile Extraction

\- ✅ Skills Detection

\- ✅ Education Detection

\- ✅ Experience Detection

\- ✅ Resume Scoring

\- ✅ Skill Matching

\- ✅ Candidate Ranking

\- ✅ CSV Export

\- ✅ JSON Export

\- ✅ Summary Table



\---



\## 🛠 Technologies Used



\- Python

\- Streamlit

\- PyMuPDF

\- python-docx

\- Pandas

\- spaCy

\- Regex



\---



\## 📁 Project Structure



```

smart\_resume\_parser/



│ app.py

│ requirements.txt

│ README.md

│ .gitignore



├── parser/

│      pdf\_parser.py

│      docx\_parser.py

│      extractor.py

│      scorer.py



├── data/

│      skills.csv



├── outputs/

│      resume\_data.csv

│      resume\_data.json



├── sample\_resumes/

│      resume1\_professional.pdf

│      resume2\_professional.pdf

│      resume3\_professional.pdf

│      resume4\_professional.pdf

│      resume5\_professional.pdf

```



\---



\## ⚙ Installation



Clone repository



```bash

git clone https://github.com/YOUR\_USERNAME/smart-resume-parser.git

```



Move into project folder



```bash

cd smart-resume-parser

```



Install dependencies



```bash

pip install -r requirements.txt

```



Download spaCy model



```bash

python -m spacy download en\_core\_web\_sm

```



Run application



```bash

streamlit run app.py

```



\---



\## 📊 Output



The parser extracts:



\- Name

\- Email

\- Phone Number

\- LinkedIn URL

\- GitHub URL

\- Skills

\- Education

\- Experience



It also generates:



\- Resume Score

\- Match Percentage

\- Candidate Ranking



Exports:



\- CSV file

\- JSON file



\---



\## 📷 Screenshots



(Add screenshots after running the application)



\---



\## 🎯 Future Enhancements



\- OCR support for scanned resumes

\- AI-based resume ranking

\- Job description matching

\- Database integration

\- Resume recommendation system

\- Dashboard analytics



\---




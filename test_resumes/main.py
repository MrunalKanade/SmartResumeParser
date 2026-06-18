from parser.pdf_parser import extract_pdf_text

path = "test_resumes/resume1.pdf"

text = extract_pdf_text(path)

print(text)
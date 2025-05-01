from pdfminer.high_level import extract_text

SKILL_KEYWORDS = [
    "Python", "Java", "SQL", "AWS", "Cloud", "Docker", "Git",
    "Machine Learning", "Flask", "Excel", "PowerPoint", "C", 
    "JavaScript", "communication", "leadership", "problem solving", 
    "time management"
]

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_skills(text):
    found_skills = []
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    
    match_score = int((len(found_skills) / len(SKILL_KEYWORDS)) * 100)
    return list(set(found_skills)), match_score


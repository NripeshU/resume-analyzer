from flask_cors import CORS
from flask import Flask, request, jsonify
import PyPDF2
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

def analyze_resume(text, job_desc):
    feedback = []
    score = 0

    text_lower = text.lower()
    job_lower = job_desc.lower()

    # Common tech keywords
    skills = ["python", "java", "c++", "flask", "machine learning", "aws", "sql", "react"]

    resume_skills = [s for s in skills if s in text_lower]
    job_skills = [s for s in skills if s in job_lower]

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    # Skill match scoring
    if job_skills:
        match_score = int((len(matched) / len(job_skills)) * 40)
    else:
        match_score = 0

    score += match_score

    # Section checks
    if "experience" in text_lower:
        score += 15
    else:
        feedback.append("Missing experience section")

    if "project" in text_lower:
        score += 15
    else:
        feedback.append("Add projects section")

    if len(text.split()) > 120:
        score += 15
    else:
        feedback.append("Resume too short")

    # Final feedback
    feedback.append(f"Matched skills: {', '.join(matched)}")
    feedback.append(f"Missing skills for job: {', '.join(missing)}")

    return feedback, score

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    job = request.form.get('job')

    text = extract_text_from_pdf(file)

    feedback, score = analyze_resume(text, job)

    return jsonify({
        "feedback": feedback,
        "score": score
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    resume = data.get('resume')
    job = data.get('job')

    feedback, score = analyze_resume(resume, job)

    return jsonify({
        "feedback": feedback,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
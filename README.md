# AI Resume Analyzer

A web app that analyzes resumes and compares them against job descriptions using keyword matching and scoring.

## Features
- Resume text analysis
- PDF resume upload
- Job description matching
- Skill detection
- Score calculation
- Visual feedback (progress bar + color-coded suggestions)

## Tech Stack
- Python (Flask)
- HTML/CSS/JavaScript
- PyPDF2

## How to Run Locally

1. Clone the repo:
   git clone https://github.com/YOUR-USERNAME/resume-analyzer.git
   cd resume-analyzer

2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate # Windows

3. Install dependencies:
   pip install flask flask-cors PyPDF2

4. Run app:
   python app.py

5. Open `index.html` in browser

## Future Improvements
- Deploy to cloud (Render/AWS)
- Better NLP analysis
- UI enhancements
- Resume scoring model

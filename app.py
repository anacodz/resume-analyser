from flask import Flask, request, render_template
from resume_parser import extract_text_from_pdf, extract_skills
import os
import sys

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            text = extract_text_from_pdf(path)

            # Optional: Print extracted text for debugging (safe encoding)
            sys.stdout.buffer.write(f"\nExtracted Text:\n{text}\n".encode("utf-8", errors="ignore"))

            skills, score = extract_skills(text)
            print(f"Matched Skills: {skills}")
            print(f"Match Score: {score}%")
            return render_template("result.html", skills=skills, score=score)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)



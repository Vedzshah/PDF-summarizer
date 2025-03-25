import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import PyPDF2
import pandas as pd

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Please check your .env file.")

genai.configure(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Function to summarize text using Gemini API
def summarize_text(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"Summarize this:\n\n{text}")
        return response.text
    except Exception as e:
        return str(e)

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

# Function to extract text from CSV
def extract_text_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()

# Route for file upload and summarization
@app.route("/", methods=["GET", "POST"])
def upload_file():
    summary = None  # Initialize summary as None
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("upload.html", error="No file part")

        file = request.files["file"]

        if file.filename == "":
            return render_template("upload.html", error="No selected file")

        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        # Process file based on type
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.filename.endswith(".csv"):
            text = extract_text_from_csv(file_path)
        else:
            return render_template("upload.html", error="Unsupported file format. Upload PDF or CSV.")

        summary = summarize_text(text)

    return render_template("upload.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)

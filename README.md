File Summarizer
This is a Flask-based web application that allows users to upload PDF and CSV files for summarization. The application extracts text from the uploaded file and generates a concise summary using the Gemini API.
----------------------------------------------------------------------------------------------------------------------------------------
Features
Upload PDF or CSV files

Extracts text from the uploaded file

Generates a summary using Google Gemini API

Simple and clean UI for file upload and viewing the summary
----------------------------------------------------------------------------------------------------------------------------------------
Tech Stack
Backend: Flask, Python

Frontend: HTML, CSS

APIs: Google Gemini AI

Libraries: PyPDF2 (for PDFs), Pandas (for CSVs), dotenv (for environment variables)
----------------------------------------------------------------------------------------------------------------------------------------
To install dependencies
pip install -r requirements.txt

Create a .env file and add your Google Gemini API Key:
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key
----------------------------------------------------------------------------------------------------------------------------------------
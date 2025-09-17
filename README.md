📄 OCR for Text Extraction
📌 Description

A Streamlit-based OCR app for extracting key details from GATE scorecard images.

Uses Tesseract OCR and OpenCV for text recognition and preprocessing.

Extracts and classifies fields like Name, Registration Number, Gender, and GATE Score.

Displays results in a table and allows download as CSV.

✨ Features

🖼 Upload GATE scorecard images (.png, .jpg, .jpeg)

🔍 Extract text with Tesseract OCR

🧹 Preprocess images using OpenCV

📊 Classify structured data: Name, Reg. No., Gender, Score

📥 Export results to CSV

⚡ Simple interactive UI built with Streamlit

🛠 Tech Stack

Python 3

Streamlit

Tesseract OCR

OpenCV

🚀 Installation & Usage

Clone the repository

git clone https://github.com/NavaneeshK-303/OCR-For-Text-Extraction.git
cd OCR-For-Text-Extraction


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate      # Windows  
source venv/bin/activate   # Linux/Mac  


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run main.py


Open the app in your browser → http://localhost:8501

📂 Project Structure
OCR-For-Text-Extraction/
│── main.py          # Core Streamlit app with OCR logic
│── frontend.py      # Additional frontend UI logic
│── requirements.txt # Python dependencies
│── README.md        # Project documentation


Pandas & NumPy

Pillow

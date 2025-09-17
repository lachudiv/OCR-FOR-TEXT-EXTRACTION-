import pytesseract
from pytesseract import Output
import cv2
import re
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from io import StringIO

# Set Tesseract path (Windows specific)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Streamlit app title
st.title('GATE Score Extractor - OCR App')

# Function to extract text from image using Tesseract OCR
def extract_text_from_image(image):
    image = np.array(image)  # Convert PIL image to NumPy array
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR (OpenCV format)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray_image, output_type=Output.STRING)
    cleaned_text = re.sub(r'[|]', '', text)  # Clean the text by removing unwanted characters
    return cleaned_text

# Function to classify extracted text into predefined fields
def classify_extracted_text(text):
    classified_data = {
        'Name': [],
        'Registration Number': [],
        'Gender': [],
        'GATE Score': []
    }

    # Regular expressions to match the fields
    name_pattern = r'Name\s*:?\s*([A-Za-z\s]+)(?=\n|Age|Address)(?!.*(?:Registration Number))'
    registration_pattern = r'ezon\s*([A-Z0-9]+)'  # Use "ezon" to capture adjacent registration numbers
    gender_pattern = r'(Male|Female)'
    score_pattern = r'GATE Score\s*([\d]+)'

    names = re.findall(name_pattern, text)
    registration_number = re.findall(registration_pattern, text)
    genders = re.findall(gender_pattern, text)
    score_match = re.findall(score_pattern, text)

    if names:
        classified_data['Name'] = [name.strip() for name in names]
    if registration_number:
        classified_data['Registration Number'] = [registration_number[0].strip()] if registration_number else []
    if genders:
        classified_data['Gender'] = genders
    if score_match:
        classified_data['GATE Score'] = [score_match[0].strip()]

    return classified_data

# Function to convert classified data to CSV and offer it for download
def convert_to_csv(classified_data):
    df = pd.DataFrame({key: pd.Series(value) for key, value in classified_data.items()})
    csv_data = df.to_csv(index=False)
    return csv_data

# Streamlit file uploader
uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

# Button to process the image and display results
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Process Image'):
        # Extract text using OCR
        extracted_text = extract_text_from_image(image)
        st.write("Extracted Text:")
        st.write(extracted_text)  # Optionally display the raw extracted text

        # Classify the extracted text
        classified_data = classify_extracted_text(extracted_text)

        # Convert the classified data to CSV
        csv_data = convert_to_csv(classified_data)

        # Display the classified data in Streamlit
        df = pd.read_csv(StringIO(csv_data))
        st.subheader('Extracted and Classified Data:')
        st.dataframe(df)

        # Provide a download button for the CSV
        st.download_button(label='Download Classified Data as CSV', data=csv_data, file_name='classified_text.csv', mime='text/csv')
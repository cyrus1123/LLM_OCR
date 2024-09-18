
# OCR Application with Tessaract and Llama3.1 (8B) 

## Overview

This application allows users to upload images for Optical Character Recognition (OCR), extracting text using Tesseract-OCR and further analyzing the text using the Llama3.1 (8B) model. The application is built with Flask, making it easy to deploy and run.

## Features

- Image upload via a web interface.
- OCR processing using Tesseract.
- Text analysis with Llama3.1 (8B) for summarization and paraphrasing.
- Simple, intuitive user interface with clear chat history functionality.

## Requirements

- Python 3.9+
- Flask
- Pillow (PIL)
- Transformers (Llama3.1)
- Torch
- Tesseract-OCR

### Python Dependencies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
System-Level Requirements
Make sure you have Tesseract-OCR installed:

bash
Copy code
sudo apt-get install tesseract-ocr
Installation

Clone the repository:
git clone https://github.com/your-repo/ocr-llama.git
cd ocr-llama
Install dependencies:


pip install -r requirements.txt
Download the Llama3.1 model weights:


python -c "from transformers import LlamaForCausalLM; LlamaForCausalLM.from_pretrained('llama-3.1-8b')"
Install Tesseract-OCR:


sudo apt-get install tesseract-ocr
Running the Application

Start the Flask application:
 
python app.py
Open the app in your browser at:
 
http://127.0.0.1:5000
Upload an image through the interface to perform OCR and view the output.
Deployment

For production, consider using Gunicorn:

 
gunicorn -w 4 app:app
You can also use Docker to containerize the app. Here’s a sample Dockerfile:

dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "4", "app:app"]
Troubleshooting

OCR Not Working: Ensure that Tesseract is installed and properly configured.
Model Download Issues: Check your internet connection and the model source.

# SmartResume Generator - Simple Guide

## Introduction

SmartResume Generator is an easy-to-use web app that helps create resumes tailored to specific job descriptions. It uses Google's Gemini AI to format and customize resumes based on the details you provide.

## Key Features

- Simple web interface built with Streamlit.
- AI-powered resume creation using Google Gemini.
- Fill in your details, and the app generates a structured resume for you.

## Getting Started

### Requirements

- Python 3.8 or later.
- A Google Gemini API key.

### Installation

First, install the required packages:

```bash
pip install streamlit google-generativeai
```

### Get Your API Key

1. Visit Google AI Studio.
2. Go to "API Keys" and generate a new key.
3. Copy and save the key.

### Set Up Your API Key

For security, store your API key in an environment variable:

#### On Windows

```bash
set GOOGLE_API_KEY=your_api_key_here
```

#### On macOS/Linux

```bash
export GOOGLE_API_KEY=your_api_key_here
```

Update your script to use the key:

```python
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

## How to Use

### Run the App

In your terminal, run:

```bash
streamlit run generator.py
```

### Steps to Generate a Resume

1. Open the link that appears in the terminal.
2. Enter your details: Name, Email, Phone, Education, Experience, Skills, and Job Description.
3. Click "Generate Resume."
4. Your resume will be displayed on the screen, ready to copy.

## Understanding the Files

- `generator.py` - The main script that runs the app.
- `requirements.txt` - Lists the required Python packages.

## Common Issues & Fixes

### Invalid API Key?

- Double-check the key from Google AI Studio.
- Make sure it is stored correctly as an environment variable.

### Weird Characters in Resume?

- The app automatically removes unsupported characters.
- If needed, manually check your input for unusual symbols.

### App Not Running?

- Check if Streamlit is installed by running `pip show streamlit`.
- Restart your terminal and try running the command again.

## Future Improvements

- Add options to download resumes as PDF or DOCX.
- Improve formatting and layout.
- Allow users to import LinkedIn profiles.

## Final Thoughts

SmartResume Generator makes it easy to create resumes in seconds. Just enter your details, and let AI handle the formatting!

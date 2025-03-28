# AskAI – Text Summarizer

A lightweight web app that summarizes user-submitted text using GPT-3.5.

## Features

- Calls OpenAI's GPT-3.5 API to summarize text  
- Simple interface: paste text and get a summary  
- Secure API key management with `.env`  
- Built with Flask and deployed locally (deployment coming soon)
- 
## How to Run

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key in a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

3. Run the app:

```bash
python app.py
```

Visit http://localhost:5000 to use the app.

## Stack

- Python 3.10
- Flask
- OpenAI Python SDK (>=1.0.0)
- HTML (basic UI)

## Project Goal

This is a personal project to explore OpenAI's API and build a functional, beginner-friendly full-stack tool.  


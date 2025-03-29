# AskAI – Text Summarizer

A lightweight, GPT-3.5-powered web tool for summarizing, translating, and analyzing text.  
Built with Flask, OpenAI API, and Bootstrap.

## Features

- **Text Summarization** – distills long text into concise summaries using GPT-3.5  
- **Translation** – converts English input into simplified Chinese  
- **Sentiment Detection** – classifies text as Positive, Negative, or Neutral  
- **.txt File Upload** – supports file-based input in addition to pasted text  
- **Clean UI** – built with Bootstrap for a smooth user experience  
- **Live on Render** – no installation needed to try it out

## Demo

Try it now:  
**[https://askai-ylt9.onrender.com](https://askai-ylt9.onrender.com)**

Paste text or upload a `.txt` file, choose a mode, and get instant results!

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

- **Backend**: Python, Flask, OpenAI SDK  
- **Frontend**: HTML, Bootstrap 5  
- **API**: GPT-3.5 (`gpt-3.5-turbo`) via OpenAI  
- **Hosting**: Render (Free Tier)

## Project Goal

This is a personal project to explore OpenAI's API and build a functional, beginner-friendly full-stack tool.  


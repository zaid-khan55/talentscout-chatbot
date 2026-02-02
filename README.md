# TalentScout – AI Hiring Assistant Chatbot

## Overview
TalentScout is an AI-powered hiring assistant chatbot built to automate the **initial screening of technical candidates**.  
It interacts with candidates, collects essential information, and generates **custom technical interview questions** based on the candidate’s declared tech stack using a Large Language Model (LLM).

The project focuses on **prompt engineering, context management, and practical LLM usage** in a real-world recruitment scenario.

---

## Problem Statement
Recruiters often spend significant time collecting candidate details and preparing initial technical screening questions.  
TalentScout reduces this effort by automating the first interaction while maintaining relevance, consistency, and professionalism.

---

## Solution
TalentScout guides candidates through a structured conversation, gathers key details, and dynamically generates technical interview questions tailored to the candidate’s skills.

The chatbot uses:
- Rule-based logic for predictable data collection
- LLMs only where intelligent reasoning is required

---

## Key Features

### 1. Candidate Information Collection
The chatbot collects:
- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Role(s)  
- Current Location  
- Tech Stack (languages, frameworks, tools)

### 2. Tech-Stack-Based Question Generation
- Generates **3–5 technical interview questions**
- Questions are tailored to the candidate’s declared tech stack
- Mix of conceptual and real-world scenario questions
- No answers or hints are provided

### 3. Context-Aware Conversation
- Maintains conversation flow using session state
- Avoids repeating questions
- Ensures a smooth chatbot-like experience

### 4. Exit Handling
- Supports graceful exit using keywords such as `exit`, `quit`, or `bye`
- Ends the conversation professionally

### 5. Data Privacy
- No permanent data storage
- Candidate information exists only during the active session
- GDPR-friendly, simulated data handling

---

## Tech Stack
- **Python**
- **Streamlit** – UI and interaction
- **OpenAI GPT** – Technical question generation
- **Streamlit Session State** – Context handling
- **Virtual Environment (venv)** – Dependency isolation

---

## Project Structure

talentscout-chatbot/
├── app.py # Main Streamlit application
├── prompts.py # System and question-generation prompts
├── utils.py # Helper utilities
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .streamlit/
└── secrets.toml # API key configuration (ignored in Git)


---
Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/talentscout-chatbot.git
cd talentscout-chatbot

2. Create & Activate Virtual Environment
python -m venv venv


Windows (PowerShell):

.\venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. Configure OpenAI API Key

Create the file:

.streamlit/secrets.toml


Add:

OPENAI_API_KEY = "your_openai_api_key_here"

5. Run the Application
python -m streamlit run app.py


The app will open at:

http://localhost:8501

Prompt Engineering Approach
System Prompt

The system prompt defines the chatbot’s role, tone, and boundaries:

Acts strictly as a hiring assistant

Maintains a professional and neutral tone

Restricted to recruitment and screening tasks only

Dynamic Prompt

The dynamic prompt:

Injects the candidate’s declared tech stack

Generates relevant technical interview questions

Ensures clarity and appropriate difficulty

This approach keeps LLM output controlled and relevant.

Design Decisions
Hybrid Architecture

Rule-based flow for collecting candidate information

LLM usage only for technical question generation

This improves:

Reliability

Predictability

Data privacy

Efficient use of AI resources

Challenges Faced & Solutions

Challenge: Maintaining conversation context
Solution: Used Streamlit session state to track steps and messages.

Challenge: Clearing user input safely
Solution: Implemented on_change callback to follow Streamlit widget lifecycle rules.

Challenge: Preventing unnecessary LLM calls
Solution: Limited AI usage to only question generation.

Future Improvements

Sentiment analysis to assess candidate confidence

Multilingual support

Resume upload and parsing

Cloud deployment (AWS / Streamlit Cloud)

Recruiter dashboard for reviewing candidate responses

Demo

A short demo video (Loom) demonstrates:

Chatbot greeting

Candidate information collection

Tech stack input

Technical question generation

Graceful exit

Conclusion

TalentScout demonstrates a practical and responsible use of Large Language Models in recruitment.
By combining structured logic with AI-driven question generation, the chatbot provides a scalable, efficient, and recruiter-friendly screening solution.

Author

Zaid Khan
AI/ML Intern Applicant

\# 🤖 TalentScout – AI Hiring Assistant Chatbot



\## 📌 Project Overview

TalentScout is an AI-powered Hiring Assistant chatbot designed to automate the \*\*initial screening of technical candidates\*\*.  

The chatbot interacts with candidates, gathers essential information, and dynamically generates \*\*tailored technical interview questions\*\* based on the candidate’s declared tech stack using a Large Language Model (LLM).



This project demonstrates practical use of \*\*prompt engineering, context handling, and UI design\*\* in a real-world recruitment scenario.



---



\## 🎯 Objectives

\- Automate first-round candidate screening

\- Reduce recruiter workload

\- Ensure consistent and scalable technical assessments

\- Demonstrate effective and controlled use of LLMs



---



\## ✨ Features



\### ✅ Candidate Interaction

\- Professional greeting and onboarding

\- Step-by-step guided conversation

\- Context-aware interaction flow



\### ✅ Information Collection

The chatbot collects the following details:

\- Full Name  

\- Email Address  

\- Phone Number  

\- Years of Experience  

\- Desired Position(s)  

\- Current Location  

\- Tech Stack (languages, frameworks, tools)



\### ✅ Tech-Stack-Based Question Generation

\- Generates \*\*3–5 technical interview questions\*\*

\- Questions are dynamically generated based on the declared tech stack

\- Mix of conceptual and real-world scenario questions

\- No answers or hints are provided



\### ✅ Conversation Management

\- Maintains context using Streamlit session state

\- Prevents repeated or irrelevant questions

\- Graceful exit handling using keywords like `exit`, `bye`, or `quit`



\### ✅ Data Privacy \& Security

\- No permanent data storage

\- Candidate data exists only during the active session

\- GDPR-compliant simulated data handling



---



\## 🛠️ Tech Stack



| Component | Technology |

|--------|-----------|

| Programming Language | Python |

| Frontend | Streamlit |

| Large Language Model | OpenAI GPT |

| State Management | Streamlit Session State |

| Environment | Virtual Environment (venv) |



---



\## 🧱 Project Structure



Talentscout-chatbot/

├── app.py

├── prompts.py

├── utils.py

├── requirements.txt

├── README.md

└── .streamlit/

└── secrets.toml





---



\## ⚙️ Installation \& Setup



\### 1️⃣ Clone the Repository

```bash

git clone https://github.com/yourusername/talentscout-chatbot.git

cd Talentscout-chatbot



2️⃣ Create \& Activate Virtual Environment

python -m venv venv





Windows (PowerShell):



.\\venv\\Scripts\\Activate.ps1



3️⃣ Install Dependencies

pip install -r requirements.txt



4️⃣ Configure OpenAI API Key



Create the following file:



.streamlit/secrets.toml





Add:



OPENAI\_API\_KEY = "your\_openai\_api\_key\_here"



5️⃣ Run the Application

python -m streamlit run app.py





The application will open in your browser at:



http://localhost:8501



🧠 Prompt Design Strategy

System Prompt



The system prompt defines:



The chatbot’s role as a hiring assistant



Professional and neutral tone



Strict limitation to recruitment-related tasks



Dynamic Prompt



Injects the candidate’s declared tech stack



Generates relevant technical interview questions



Ensures clarity, relevance, and consistency



This controlled prompt design minimizes hallucinations and keeps the chatbot aligned with its purpose.



🧩 Architecture \& Design Decisions

Hybrid Logic Approach



Rule-based logic for candidate information collection



LLM usage only for technical question generation



This approach ensures:



Predictability and reliability



Reduced AI misuse



Better privacy and control



Efficient use of LLM resources



🔐 Data Privacy \& Compliance



No candidate data is stored permanently



No external databases or logging systems are used



All data exists only in Streamlit session memory



Fully compliant with GDPR best practices



⚠️ Challenges \& Solutions

Challenge: Maintaining conversation context



Solution: Used Streamlit session\_state to track steps, messages, and candidate data.



Challenge: Clearing user input safely



Solution: Used Streamlit’s on\_change callback to reset input without violating widget lifecycle rules.



Challenge: Avoiding unnecessary LLM usage



Solution: Adopted a hybrid rule-based + AI architecture.



🚀 Future Enhancements



Sentiment analysis to gauge candidate confidence



Multilingual support



Resume upload and parsing



Cloud deployment (AWS / Streamlit Cloud)



Recruiter dashboard



🎥 Demo



A short demo video (via Loom) can demonstrate:



Chatbot greeting



Candidate information collection



Tech stack declaration



Technical question generation



Graceful conversation exit



🏁 Conclusion



TalentScout demonstrates how Large Language Models can be effectively integrated into recruitment workflows while maintaining control, privacy, and relevance.

The project balances structured logic with AI capabilities, making it scalable and recruiter-friendly.



👤 Author



Zaid Khan

AI/ML Intern Applicant


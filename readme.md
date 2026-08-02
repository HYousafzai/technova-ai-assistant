AI Chatbot Development

An intelligent, full-stack AI customer support chatbot built with **FastAPI**, **Google Gemini API**, and a clean, modern **HTML/CSS/JS** frontend interface.

---

 Features

- **Real-Time AI Responses**: Powered by Google's Gemini Flash model (`gemini-3.6-flash`).
- **Multi-Turn Chat History**: Retains session-based conversation context for natural dialogues.
- **Modern Responsive UI**: Lightweight, interactive frontend with clean styling.
- **FastAPI Backend**: Asynchronous Python backend handling API routing, CORS, and static file serving.
- **Environment Security**: Secure API key management via `.env`.

---

##  Project Structure

```text
week2(project1)/
│
├── main.py              # FastAPI application server & Gemini API integration
├── requirements.txt     # Python package dependencies
├── .env                 # Environment variables (API Key) - DO NOT COMMIT TO GIT
├── .gitignore           # Files and folders ignored by Git
└── static/              # Web frontend directory
    ├── index.html       # Chatbot interface
    ├── style.css        # CSS styling
    └── script.js        # Frontend API call logic


    Getting Started

    Prerequisites
Python 3.10+ installed
A Google Gemini API key (Get a free key from Google AI Studio)

1. Clone the Repository
Bash
git clone [https://github.com/HYousafzai/technova-ai-assistant.git](https://github.com/HYousafzai/technova-ai-assistant.git)
cd technova-ai-assistant


2. Set Up Virtual Environment
Bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Bash
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the root folder of the project:

Code snippet
GEMINI_API_KEY=your_actual_gemini_api_key_here

Running the Application
Launch the local development server with Uvicorn:

Bash
uvicorn main:app --reload
Open your web browser and navigate to:
👉 http://127.0.0.1:8000

API Endpoints
POST /api/chat
Sends a user prompt to the chatbot backend.

Request Payload:
JSON
{
  "message": "Give me some skincare tips",
  "session_id": "optional-uuid-string"
}

Response Payload:
JSON
{
  "response": "Here are a few essential skincare tips...",
  "session_id": "uuid-string"
}


Tech Stack
Backend Framework: FastAPI + Uvicorn

AI SDK: Google GenAI SDK (google-genai)

Frontend: HTML5, CSS3, Vanilla JavaScript

Environment Management: python-dotenv

# AI-Powered IT Helpdesk System

An enterprise-grade IT Helpdesk automation platform that uses **ServiceNow**, **FastAPI**, and **Gemini AI** to automatically classify, prioritize, assign, and suggest resolutions for IT support tickets — without any manual intervention.

## Project Overview

When a user submits an IT support ticket in ServiceNow, the system:

1. Triggers a Business Rule automatically
2. Sends ticket data to the FastAPI backend via REST API
3. Gemini AI analyzes the issue
4. AI predicts category, priority, assignment group, and solution
5. ServiceNow auto-updates the ticket with AI results
6. Email notification sent for critical incidents
7. Dashboard reflects updated metrics in real time

---

## Architecture

```
User submits ticket (Service Portal)
        ↓
ServiceNow Incident Table
        ↓
Business Rule triggers (after insert)
        ↓
REST API call → FastAPI Backend (Render)
        ↓
Gemini 2.5 Flash AI Analysis
        ↓
JSON Response:
  - category
  - priority
  - assignment_group
  - solution
        ↓
ServiceNow auto-updates ticket fields
        ↓
Email Notification (Critical incidents)
        ↓
AI Helpdesk Dashboard updated
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| ServiceNow (PDI) | Workflow platform, incident management |
| FastAPI | Python backend REST API server |
| Gemini 2.5 Flash | AI analysis and ticket classification |
| Python 3.14 | Backend language |
| google-genai | Gemini API SDK |
| Render | Cloud deployment |
| ngrok | Local tunnel for testing |
| GitHub | Version control |

---

## Features

### Core Features
- **AI Ticket Classification** — Gemini AI predicts category (Network, Hardware, Security, Software)
- **Smart Priority Assignment** — AI determines Critical / High / Medium / Low
- **Auto Team Routing** — Tickets auto-assigned to Network Team, Security Team, Hardware Team, Software Team, or IT Support
- **AI Solution Suggestion** — Gemini provides a 1-2 sentence fix suggestion added to ticket comments
- **Business Rule Automation** — Zero manual intervention after ticket submission

### ServiceNow Features
- **SLA Management** — Resolution SLAs defined per priority level (Critical: 1hr, High: 4hr, Medium: 8hr, Low: 3 days)
- **Email Notifications** — Automatic alerts for critical incidents
- **Service Portal** — User-friendly ticket submission interface
- **Dashboards & Reports** — Incidents by category, priority, and assignment group

---

## Project Structure

```
ai-helpdesk-project/
│
├── backend/
│   ├── main.py              # FastAPI server
│   ├── ai_classifier.py     # Gemini AI classifier
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # API keys (not uploaded)
│
├── screenshots/             # Project screenshots
│
└── README.md
```

---

## Setup Guide

### Prerequisites
- Python 3.10+
- ServiceNow Personal Developer Instance (PDI)
- Gemini API key from [aistudio.google.com](https://aistudio.google.com)

### 1. Clone the Repository

```bash
git clone https://github.com/SaiKrishna-art/AI_IT_Helpdesk.git
cd AI_IT_Helpdesk/backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the `backend` folder:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

Server runs at: `http://127.0.0.1:8000`

API docs available at: `http://127.0.0.1:8000/docs`

---

## API Usage

### POST /analyze

Analyzes an IT support ticket and returns AI classification.

**Request:**
```json
{
  "short_description": "Laptop infected with virus",
  "description": "Suspicious popups appearing and system is very slow"
}
```

**Response:**
```json
{
  "category": "Security",
  "priority": "Critical",
  "assignment_group": "Security Team",
  "solution": "Isolate the infected laptop from the network immediately. Run a full system scan with antivirus software and remove all detected threats."
}
```

---

## ServiceNow Configuration

### Business Rules
| Rule | Trigger | Purpose |
|---|---|---|
| Auto Assign Incident | Before Insert | Keyword-based team routing |
| AI Ticket Analyzer | After Insert | Calls FastAPI, updates ticket with AI results |

### Assignment Groups
- Network Team
- Hardware Team
- Security Team
- Software Team
- IT Support

### SLA Definitions
| Priority | Resolution Time |
|---|---|
| Critical | 1 Hour |
| High | 4 Hours |
| Medium | 8 Hours |
| Low | 3 Days |

---

## AI Classification Examples

| Issue | Category | Priority | Team |
|---|---|---|---|
| WiFi disconnected | Network | Medium | Network Team |
| Virus detected on laptop | Security | Critical | Security Team |
| Laptop fan making noise | Hardware | Low | Hardware Team |
| Outlook not syncing | Software | Medium | Software Team |
| VPN keeps dropping | Network | High | Network Team |

---

## Deployment

Backend is deployed on **Render** (free tier).

> Note: Free tier has a cold start delay of ~30-50 seconds after inactivity. Subsequent requests are fast.

To deploy your own instance:
1. Fork this repository
2. Create a new Web Service on [render.com](https://render.com)
3. Set Root Directory to `backend`
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Add environment variable: `GEMINI_API_KEY`

---

## Dashboard

The AI Helpdesk Dashboard in ServiceNow includes:
- Incidents by Category (Pie chart)
- Incidents by Priority (Bar chart)
- Incidents by Assignment Group (Bar chart)

---

## Future Improvements

- Voice-based ticket submission
- Sentiment analysis to detect frustrated users
- AI chatbot via ServiceNow Virtual Agent
- Predictive analytics for recurring issues
- Multi-language ticket support
- Auto-resolution for known issues

---

## Author

**Murthy Sai Krishna**  
B.Tech AI & Data Science — KL University  
ServiceNow Certified System Administrator (CSA)  
[LinkedIn](https://www.linkedin.com/in/murthy-sai-krishna/) | [GitHub](https://github.com/SaiKrishna-art)

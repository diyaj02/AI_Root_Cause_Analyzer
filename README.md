# AI Incident Root Cause Analyzer

An AI-assisted DevOps tool that analyzes system incidents using rule-based logic and machine learning to identify root causes, estimate confidence levels, and suggest remediation actions.

This project simulates how modern cloud monitoring systems assist engineers by automatically diagnosing infrastructure issues from operational metrics.

---

## Overview

The **AI Incident Root Cause Analyzer** helps developers and DevOps engineers quickly understand system failures.

The application takes incident metrics such as:

- CPU usage
- Memory usage
- Error type
- Deployment status

and produces:

- Detected root causes
- Confidence score
- AI explanation
- Machine learning prediction
- Recommended actions

The system combines rule-based expert logic with a machine learning assistant and an interactive frontend dashboard.

---

## Key Features

- Rule-based incident diagnosis engine
- Machine learning assisted root cause prediction
- Human-readable AI explanations
- Confidence scoring system
- Automated remediation suggestions
- Interactive web dashboard
- REST API powered backend

---

## Project Structure

AI-Incident-Root-Cause-Analyzer/
│
├── backend/
│ ├── analyzer.py # Core AI logic and ML assistant
│ ├── app.py # Flask backend API
│
├── frontend/
│ ├── index.html # Interactive UI
│ ├── style.css # Dashboard styling
│
├── README.md
└── .gitignore


---

## Technologies and Modules Used

### Backend
- Python
- Flask
- Flask-CORS
- NumPy
- scikit-learn (LogisticRegression)

### Frontend
- HTML5
- CSS3
- JavaScript
- Canvas API for animated background

### AI and Logic Components
- Rule-Based Expert System
- Logistic Regression Model
- Confidence Weighting System
- Incident Pattern Analysis

---

## How It Works

### Rule-Based Analysis

The system evaluates incident inputs against predefined diagnostic rules:

- High CPU after deployment may indicate deployment-related issues
- High memory usage with timeout errors may indicate memory leaks
- Extremely high CPU and memory usage may indicate resource exhaustion

Each rule contributes to a weighted confidence score.

---

### Machine Learning Assistant

A Logistic Regression model analyzes incident features:

[CPU, Memory, Error Flag, Deployment Flag]


and predicts likely failure categories such as:

- Normal
- Bad Deployment
- Memory Leak
- Resource Exhaustion

---

### Explanation Engine

The analyzer generates human-readable explanations and remediation suggestions to simulate an AI-assisted DevOps diagnostic workflow.

---

## API Endpoints

### `GET /`

Checks backend status.

### `POST /analyze`

Analyzes an incident.

#### Example Request

```json
{
  "cpu": 90,
  "memory": 85,
  "error": "TimeoutException",
  "recent_deployment": true
}

Example Response 
{
  "confidence": "High",
  "root_causes": ["Bad deployment causing CPU spike"],
  "explanation": "...",
  "ml_prediction": "Bad Deployment",
  "recommended_actions": ["Rollback recent deployment"]
}


Running the Project

Install Dependencies
pip install flask flask-cors numpy scikit-learn

Start Backend
cd backend
python app.py

The server runs at:
http://127.0.0.1:5000

Launch Frontend

Open:
frontend/index.html
using Live Server or directly in a browser.

## Use Cases

- DevOps incident analysis and troubleshooting
- AI-assisted monitoring and diagnostics simulation
- Cloud engineering and infrastructure demonstration projects
- Academic AI/ML learning and experimentation
- Portfolio-ready engineering showcase

---

## Future Improvements

- Integration with cloud monitoring platforms (Azure Monitor, AWS CloudWatch, etc.)
- Real-time log ingestion and telemetry processing
- Interactive data visualization dashboards
- Advanced anomaly detection using deep learning models
- User authentication and role-based access control

License

This project is intended for educational and demonstration purposes. 
# LogMind AI — Smart Log Analysis System

LogMind AI is a web-based application that analyzes log files to identify errors and potential anomalies. It uses predefined rules to process log entries and displays the results through a dashboard.

## Features

- Upload `.log` and `.txt` files.
- Detect errors and potential anomalies.
- View log statistics and anomaly rates.
- Identify affected services.
- Display analysis results on a dashboard.

## Technology Stack

- **Frontend:** React.js, Vite, CSS
- **Backend:** Python, FastAPI, Uvicorn
- **Data Exchange:** JSON
- **Testing Data:** Sample log files and HDFS log dataset

## How It Works

Users upload a log file through the frontend. The backend processes the file using predefined rules, identifies potential issues, and returns the analysis results to the dashboard.

## How to Run

The project requires Python 3, Node.js, and npm. Clone the repository, install the backend dependencies from `backend/requirements.txt`, and start the FastAPI server. Then install the frontend dependencies in the `frontend` folder and start the application using Vite.

## Limitations

The current system relies on predefined rules and may not detect complex or previously unseen anomalies. Further testing is needed to evaluate its performance with larger datasets.

## Future Scope

Future improvements may include machine-learning-based anomaly detection, AI-assisted log explanations, and real-time monitoring.

## GitHub Repository

https://github.com/saivaishnavi30/LogMind-AI

---

*LogMind AI — Making log analysis simpler and more accessible.*

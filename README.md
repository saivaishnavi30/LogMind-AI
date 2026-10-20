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

Users upload a `.log` or `.txt` file through the React frontend. The FastAPI backend processes the log entries using predefined rules to identify errors and potential anomalies. The results, including summary statistics and affected services, are displayed on the dashboard.

```text
User Uploads Log File
         ↓
React Frontend
         ↓
FastAPI Backend
         ↓
Log Processing
         ↓
Rule-Based Analysis
         ↓
Generate Analysis Results
         ↓
Display Results on Dashboard
```

## How to Run

The project requires Python 3, Node.js, and npm.

1. Clone the GitHub repository.
2. Install the backend dependencies from `backend/requirements.txt`.
3. Start the FastAPI backend server.
4. Open a second terminal and navigate to the `frontend` folder.
5. Install the frontend dependencies and start the application using Vite.
6. Open the local URL displayed in the terminal to access LogMind AI.


## Limitations

The current system relies on predefined rules and may not detect complex or previously unseen anomalies. Further testing is needed to evaluate its performance with larger datasets.

## Future Scope

Future improvements may include machine-learning-based anomaly detection, AI-assisted log explanations, and real-time monitoring.

## GitHub Repository

https://github.com/saivaishnavi30/LogMind-AI

---

*LogMind AI — Making log analysis simpler and more accessible.*

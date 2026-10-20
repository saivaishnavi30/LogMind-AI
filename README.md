# LogMind AI — Smart Log Analysis System

LogMind AI is a web-based log analysis application designed to simplify log monitoring by identifying potential errors and anomalies in uploaded log files. It processes log entries using predefined rules and presents the results through an interactive dashboard.

The application helps developers and system administrators review log data, understand potential issues, and identify services that may require further investigation.

## 🚀 Features

- **Log File Upload:** Upload `.log` and `.txt` files for analysis.
- **Automated Log Analysis:** Process log entries using predefined rules.
- **Error Detection:** Identify log entries classified as errors.
- **Anomaly Detection:** Detect entries matching predefined anomaly conditions.
- **Summary Statistics:** Display log counts, errors, anomalies, and anomaly rate.
- **Service Analysis:** Summarize log entries associated with affected services.
- **Interactive Dashboard:** Present analysis results in a structured interface.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | React.js |
| Frontend Build Tool | Vite |
| Styling | CSS |
| Backend | Python |
| Backend Framework | FastAPI |
| Server | Uvicorn |
| Data Exchange | JSON |
| Testing Data | Sample log files and HDFS log dataset |

## 🏗️ System Architecture

The application follows a frontend–backend architecture.

1. **User Interface:** The React frontend allows users to upload log files and view results.
2. **Backend Processing:** The FastAPI backend receives the uploaded files and processes their contents.
3. **Log Analysis:** Predefined rules are applied to identify errors and potential anomalies.
4. **Report Generation:** Summary statistics and service-level information are returned to the frontend.
5. **Results Display:** The dashboard presents the generated analysis report.

## 📂 Project Structure

```text
LogMind-AI/
├── backend/
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
├── data/
│   ├── test.log
│   └── logmind.db
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── .gitignore
```

## ⚙️ Prerequisites

Install the following before running the project:

- Python 3
- Node.js and npm
- Git

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saivaishnavi30/LogMind-AI.git
cd LogMind-AI
```

### 2. Set Up the Backend

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activate it using:

```bash
venv\Scripts\activate
```

Install the backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the backend server from the project root:

```bash
uvicorn backend.app:app --reload
```

The backend will typically be available at:

`http://localhost:8000`

FastAPI API documentation:

`http://localhost:8000/docs`

### 3. Set Up the Frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite, typically:

`http://localhost:5173`

Keep both the backend and frontend servers running while using the application.

## 🔍 How to Use

1. Open LogMind AI in your browser.
2. Select a supported `.log` or `.txt` file.
3. Upload the file for analysis.
4. Allow the backend to process the log entries.
5. Review the generated statistics, detected errors, potential anomalies, and affected services.

## 🧪 Testing

The application can be tested with sample log files containing different types of log entries. Verify that the file upload, log processing, detection rules, statistics generation, and results display operate as expected.

Testing with larger datasets and labelled log data can help evaluate detection accuracy and processing performance.

## ⚠️ Current Limitations

- Detection relies on predefined rules.
- Complex or previously unseen anomalies may not be detected.
- The current implementation does not include a trained machine-learning or generative AI model.
- Further evaluation is needed for large-scale processing and detection accuracy.

## 🔮 Future Enhancements

- Machine-learning-based anomaly detection.
- Generative AI-assisted log explanations.
- Advanced root-cause analysis.
- Real-time log monitoring.
- Automated alerts for critical issues.
- Improved scalability for large log datasets.

## 🎯 Project Objective

The objective of LogMind AI is to provide a simple and accessible platform for analyzing log files, highlighting potential issues, and presenting useful summaries that reduce the effort required for manual log inspection.

## 👨‍💻 Repository

**GitHub:** https://github.com/saivaishnavi30/LogMind-AI

---

*LogMind AI — Making log analysis simpler and more accessible.*

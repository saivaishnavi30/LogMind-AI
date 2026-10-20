from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import re
import tempfile
import os

app = FastAPI(title="LogMind AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "data/logmind.db"


@app.get("/")
def home():
    return {"message": "LogMind AI API is running"}


@app.get("/api/analyze")
def analyze_demo_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    total = cursor.execute("SELECT COUNT(*) FROM logs").fetchone()[0]
    anomalies = cursor.execute(
        "SELECT COUNT(*) FROM logs WHERE status='anomaly'"
    ).fetchone()[0]
    warnings = cursor.execute(
        "SELECT COUNT(*) FROM logs WHERE status='warning'"
    ).fetchone()[0]
    errors = cursor.execute(
        "SELECT COUNT(*) FROM logs WHERE level IN ('ERROR','CRITICAL')"
    ).fetchone()[0]

    services = cursor.execute("""
        SELECT service, COUNT(*)
        FROM logs
        WHERE status='anomaly'
        GROUP BY service
        ORDER BY COUNT(*) DESC
    """).fetchall()

    conn.close()

    return {
        "filename": "Demo Database",
        "total_logs": total,
        "anomalies": anomalies,
        "warnings": warnings,
        "errors": errors,
        "anomaly_rate": round(anomalies / total * 100, 2),
        "affected_services": [
            {"service": s, "count": c} for s, c in services
        ],
        "root_cause": "Repeated service and database failures detected.",
        "recommendation": "Check database connectivity, network availability and affected services."
    }


@app.post("/api/analyze-upload")
async def analyze_upload(file: UploadFile = File(...)):

    if not file.filename.lower().endswith((".log", ".txt")):
        raise HTTPException(
            status_code=400,
            detail="Only .log and .txt files are supported."
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    text = content.decode("utf-8", errors="ignore")
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    levels = {
        "INFO": 0,
        "WARNING": 0,
        "WARN": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    services = {}

    for line in lines:
        upper = line.upper()

        for level in levels:
            if re.search(rf"\b{level}\b", upper):
                levels[level] += 1

        match = re.search(
            r"\b(?:INFO|WARNING|WARN|ERROR|CRITICAL)\s+([\w.$-]+)",
            line,
            re.IGNORECASE
        )

        if match:
            service = match.group(1)
            services[service] = services.get(service, 0) + 1

    errors = levels["ERROR"] + levels["CRITICAL"]
    warnings = levels["WARNING"] + levels["WARN"]

    anomaly_lines = errors + warnings
    anomaly_rate = round(
        anomaly_lines / len(lines) * 100, 2
    ) if lines else 0

    if errors > 0:
        root_cause = "Error and critical events were detected in the uploaded logs."
        recommendation = (
            "Review the affected services and investigate repeated "
            "ERROR/CRITICAL messages."
        )
    elif warnings > 0:
        root_cause = "Warning events indicate potentially abnormal system behavior."
        recommendation = "Investigate repeated warnings before they become failures."
    else:
        root_cause = "No significant error pattern was detected."
        recommendation = "System appears stable based on the uploaded log."

    return {
        "filename": file.filename,
        "total_logs": len(lines),
        "anomalies": anomaly_lines,
        "warnings": warnings,
        "errors": errors,
        "anomaly_rate": anomaly_rate,
        "affected_services": [
            {"service": name, "count": count}
            for name, count in sorted(
                services.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
        ],
        "root_cause": root_cause,
        "recommendation": recommendation
    }

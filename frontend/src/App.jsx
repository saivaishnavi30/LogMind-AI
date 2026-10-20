import { useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeLog = async () => {
    if (!file) return;

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(`${API}/api/analyze-upload`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Analysis failed");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div className="brand">
          <div className="logo">L</div>
          <div>
            <h1>LogMind AI</h1>
            <p>Intelligent Log Analysis</p>
          </div>
        </div>
      </header>

      <main className="container">

        {!result && (
          <>
            <section className="hero">
              <div className="eyebrow">LOG ANALYTICS</div>
              <h2>Find problems in your logs.</h2>
              <p>
                Upload an application or server log and LogMind AI
                will analyze errors, warnings and suspicious activity.
              </p>
            </section>

            <section className="upload-card">
              <div className="upload-icon">↑</div>

              <h3>Upload your log file</h3>

              <p>
                Select a <strong>.log</strong> or <strong>.txt</strong> file
              </p>

              <label className="file-button">
                Choose Log File
                <input
                  type="file"
                  accept=".log,.txt"
                  onChange={(e) => {
                    setFile(e.target.files[0]);
                    setError("");
                  }}
                />
              </label>

              {file && (
                <div className="selected-file">
                  <span>📄 {file.name}</span>
                  <button onClick={() => setFile(null)}>Remove</button>
                </div>
              )}

              <button
                className="analyze-button"
                disabled={!file || loading}
                onClick={analyzeLog}
              >
                {loading ? "Analyzing..." : "Analyze Log"}
              </button>

              {error && <div className="error">{error}</div>}
            </section>

            <section className="features">
              <div>
                <strong>01</strong>
                <h3>Detect</h3>
                <p>Find errors and abnormal events.</p>
              </div>

              <div>
                <strong>02</strong>
                <h3>Analyze</h3>
                <p>Identify affected services and patterns.</p>
              </div>

              <div>
                <strong>03</strong>
                <h3>Report</h3>
                <p>Get a clear technical summary.</p>
              </div>
            </section>
          </>
        )}

        {result && (
          <section className="report">

            <div className="report-heading">
              <div>
                <div className="eyebrow">ANALYSIS COMPLETE</div>
                <h2>Log Analysis Report</h2>
                <p>{result.filename}</p>
              </div>

              <button
                className="new-analysis"
                onClick={() => {
                  setResult(null);
                  setFile(null);
                }}
              >
                New Analysis
              </button>
            </div>

            <div className="stats">
              <Stat title="Total Logs" value={result.total_logs} />
              <Stat
                title="Anomalies"
                value={result.anomalies}
                danger
              />
              <Stat
                title="Errors"
                value={result.errors}
                danger
              />
              <Stat
                title="Anomaly Rate"
                value={`${result.anomaly_rate}%`}
              />
            </div>

            <div className="report-grid">

              <div className="report-card">
                <h3>Root Cause</h3>
                <p>{result.root_cause}</p>
              </div>

              <div className="report-card">
                <h3>Recommended Action</h3>
                <p>{result.recommendation}</p>
              </div>

            </div>

            <div className="report-card">
              <h3>Affected Services</h3>

              {result.affected_services.length === 0 ? (
                <p>No specific services identified.</p>
              ) : (
                <div className="service-list">
                  {result.affected_services.map((item) => (
                    <div className="service-row" key={item.service}>
                      <span>{item.service}</span>
                      <strong>{item.count}</strong>
                    </div>
                  ))}
                </div>
              )}
            </div>

          </section>
        )}
      </main>
    </div>
  );
}

function Stat({ title, value, danger }) {
  return (
    <div className="stat">
      <span>{title}</span>
      <strong className={danger ? "danger" : ""}>{value}</strong>
    </div>
  );
}

export default App;

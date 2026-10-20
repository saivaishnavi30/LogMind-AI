import sqlite3

DB_PATH = "data/logmind.db"


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            service TEXT,
            level TEXT,
            message TEXT,
            status TEXT
        )
    """)

    logs = [
        ("2026-10-05 09:10:12", "AuthService", "INFO",
         "User authentication service started", "normal"),

        ("2026-10-05 09:11:04", "APIService", "INFO",
         "GET /api/users request received", "normal"),

        ("2026-10-05 09:12:15", "Database", "WARNING",
         "Database response time exceeded threshold", "warning"),

        ("2026-10-05 09:13:27", "Database", "ERROR",
         "Database connection timeout", "anomaly"),

        ("2026-10-05 09:13:28", "UserService", "ERROR",
         "Failed to fetch user data", "anomaly"),

        ("2026-10-05 09:14:02", "APIService", "ERROR",
         "Request failed with status code 500", "anomaly"),

        ("2026-10-05 09:15:10", "PaymentService", "INFO",
         "Payment request processed successfully", "normal"),

        ("2026-10-05 09:16:42", "Network", "WARNING",
         "Network latency is higher than normal", "warning"),

        ("2026-10-05 09:17:08", "Network", "ERROR",
         "Connection to external service failed", "anomaly"),

        ("2026-10-05 09:18:33", "System", "CRITICAL",
         "Service unavailable after repeated failures", "anomaly"),
    ]

    cursor.executemany("""
        INSERT INTO logs
        (timestamp, service, level, message, status)
        VALUES (?, ?, ?, ?, ?)
    """, logs)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("LogMind database created successfully.")

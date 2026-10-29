# MENDR — Machine Task Manager & Health Monitor
**Team VYPERX | Open Innovation Track**

MENDR is an OS-style industrial task manager and real-time machine health monitor designed to replace traditional calendar maintenance with parameter-driven, usage-based intelligence.

## Project Structure
```text
mendr_app_prototype/
├── app.py                 # Flask Backend & Telemetry Simulation
├── requirements.txt       # Python Dependencies
└── templates/
    └── dashboard.html     # OS-Style Task Manager Web UI
```

## How to Run Locally
1. Install Python 3.x
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to: `http://127.0.0.1:5000`

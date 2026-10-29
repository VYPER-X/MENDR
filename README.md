
# MENDR — Machine Task Manager & Health Monitor

**Team VYPERX | Open Innovation Track | Hack The Circle**

MENDR is an OS-style industrial machine task manager and real-time health monitoring prototype. It helps operators monitor machine conditions, identify abnormal readings, and view active alerts from a single dashboard.

Our goal is to move industrial maintenance from fixed calendar schedules towards maintenance decisions informed by machine usage and wear.

## The Problem

Traditional maintenance approaches can make it difficult to identify machine health issues early. Fixed servicing schedules may lead to unnecessary maintenance, while unexpected machine failures can cause downtime, safety risks, and additional costs.

## Our Solution

MENDR combines machine telemetry, health scoring, status classification, and an alert dashboard to make machine conditions easier to understand.

The prototype currently uses simulated machine readings to demonstrate this workflow.

## Key Features

- **Live dashboard updates:** Machine readings refresh automatically in the browser.
- **Machine health monitoring:** Displays temperature, vibration, power readings, and health scores.
- **Status classification:** Categorizes machines as HEALTHY, WARNING, or ALERT using defined thresholds.
- **Active alerts panel:** Highlights machines requiring attention and displays their readings and health scores.
- **Centralized monitoring:** Presents multiple machines in one interface.

## How It Works

1. Simulated telemetry generates machine readings.
2. The backend evaluates temperature and vibration against configured thresholds.
3. A health score is calculated from temperature and vibration readings.
4. The dashboard refreshes and displays the latest values and machine statuses.
5. The active alerts panel highlights machines classified as WARNING or ALERT.

## Current Prototype Status

**Implemented**
- Flask backend
- Simulated machine telemetry
- Temperature and vibration status thresholds
- Rule-based machine health scoring
- Browser dashboard with automatic updates
- Active machine alerts panel

**Planned Future Improvements**
- Integration with real industrial sensors and IoT devices
- Configurable thresholds for different machine types
- Maintenance task and work-order management
- Historical data storage and trend analysis
- Predictive maintenance using validated historical data

> **Important:** The current prototype uses simulated telemetry. It does not yet demonstrate live sensor integration or validated predictive-maintenance models. The health scores and thresholds are illustrative and should not be treated as industrial safety limits.

## Technology Stack

**Currently implemented**
- Python
- Flask
- HTML
- CSS
- JavaScript

**Potential future technologies**
- MQTT or HTTP for device communication
- SQLite or PostgreSQL for historical data storage
- Analytics and predictive-maintenance models

Future technologies are proposals, not part of the current implementation unless explicitly added.

## Project Structure

```text
MENDR/
├── app.py
├── requirements.txt
└── templates/
    └── dashboard.html
```

## Run Locally

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VYPER-X/MENDR.git
   ```

2. Open the project folder:

   ```bash
   cd MENDR
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open this address in your browser:

   `http://127.0.0.1:5000`

## Team

**Team VYPERX**

- Dhruv Yadav
- Aasheesh Ayushman Panda
- Disha Tiwari

**Track:** Open Innovation

**Repository:** https://github.com/VYPER-X/MENDR

---

*Built as a hackathon prototype to explore smarter, usage-informed industrial maintenance.*

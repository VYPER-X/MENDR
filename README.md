# MENDR
OS-Style Machine Task Manager &amp; Real-Time Health Monitor — Team VYPERX hackathon project.

# MENDR — Machine Health Monitoring System

**Team:** VYPERX  
**Track:** Open Innovation

## Problem Statement

Industrial machines can develop faults due to abnormal temperature,
vibration, or power usage. Without continuous monitoring, these
issues may go unnoticed and lead to unexpected downtime or
unnecessary maintenance.

## Proposed Solution

MENDR is a machine health monitoring concept designed to help
operators observe machine parameters, identify abnormal readings,
and make better-informed maintenance decisions.

## Current Prototype

The current prototype is built using Python and Flask. It provides
a dashboard displaying sample machine information and an API that
returns simulated telemetry.

Current features:
- Displays multiple machines and their readings.
- Simulates changing temperature and vibration values.
- Provides a telemetry API at `/api/telemetry`.
- Demonstrates the concept of monitoring machine conditions.

**Important:** The readings are simulated. The current prototype
does not connect to physical sensors or industrial equipment.
Machine status and health values are illustrative and do not
automatically recalculate from every telemetry update.

## Proposed Future Improvements

- Calculate machine status using configurable thresholds.
- Recalculate health indicators from machine readings.
- Add maintenance alerts and work-order management.
- Store historical readings for trend analysis.
- Explore database integration and communication with real
  sensors or industrial gateways.
- Evaluate predictive maintenance after collecting and validating
  sufficient historical data.

## Technology Stack

### Currently implemented
- Python
- Flask
- HTML dashboard
- Simulated telemetry

### Potential future technologies
- React for a richer dashboard.
- FastAPI or an equivalent backend API.
- SQLite or PostgreSQL for historical data.
- MQTT or HTTP for device communication.

These future technologies are proposals, not implemented features.

## Run Locally

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open this address in your browser:

   http://127.0.0.1:5000

## Limitations

This is an early-stage concept prototype using simulated data.
Real sensor integration, validated predictive maintenance,
automated alerts, and automated work orders are not yet
implemented.

## Team

- Dhruv Yadav
- Aasheesh Ayushman Panda
- Disha Tiwari

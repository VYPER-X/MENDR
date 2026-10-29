# MENDR
OS-Style Machine Task Manager &amp; Real-Time Health Monitor — Team VYPRX hackathon project.
# MENDR — Machine Health Intelligence

**Team:** VYPRX  
**Track:** Open Innovation  
**Project status:** Concept / proposed design

## Problem
Industrial equipment can operate with limited visibility into power draw, load, temperature, and vibration. This can delay intervention, contribute to avoidable downtime, and make maintenance less responsive to actual operating conditions.

## Proposed solution
MENDR is a proposed OS-style machine task manager and real-time health-monitoring dashboard. It would collect machine readings, compare them with asset-specific limits, show normal/elevated/critical states, and guide operators through a maintenance response workflow.

## Proposed architecture
1. **Data input:** machine sensors or a PLC / IoT gateway.
2. **Data transfer:** MQTT or HTTP to a backend service.
3. **Rule engine:** compare readings with configurable, asset-specific thresholds and log events.
4. **Dashboard:** display readings, status, and warnings.
5. **Response workflow:** operator reviews the warning and creates or confirms a maintenance work order.

## Proposed technology stack
- Dashboard: React
- Backend/API and threshold logic: Python with FastAPI
- Storage: SQLite for an early demonstration; PostgreSQL if a more durable deployment is needed
- Device messaging: MQTT or HTTP

These are proposed choices, not claims that the system has already been implemented. The team should finalize the stack based on its skills and available hardware.

## Feasibility and validation plan
- Start with simulated readings or a controlled test data source.
- Test normal, elevated, and critical conditions against known thresholds.
- Verify event logging and the operator work-order flow.
- Connect real equipment only after safe testing and access approval.
- Treat predictive maintenance as future work until sufficient historical data is available and the model has been validated.

## Privacy and security
- Authenticate devices and users.
- Use encrypted communication where supported.
- Restrict access by role and maintain audit logs.
- Keep sensitive industrial telemetry out of public demo data.
- Publish only synthetic/sample readings unless the data owner explicitly approves disclosure.

## Current status and limitations
This repository README describes the concept and proposed implementation plan. The presentation's machine readings are illustrative. Live sensor integration, automated alerts, and work-order automation should not be represented as completed unless and until they are implemented and tested.

## Team
- Dhruv Yadav
- Aasheesh Ayushman Panda
- Disha Tiwari

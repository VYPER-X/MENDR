from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def calculate_status(temp, vibration):
    if temp >= 90 or vibration >= 6.0:
        return "ALERT"
    elif temp >= 80 or vibration >= 3.0:
        return "WARNING"
    else:
        return "HEALTHY"


# Simulated machine assets registry matching MENDR task manager
machines_db = [
    {"id": "M-101", "name": "Conveyor Motor A", "temp": 74.2, "vibration": 1.2, "power": 14.5, "status": "HEALTHY", "health": 98},
    {"id": "M-102", "name": "Hydraulic Press B", "temp": 88.6, "vibration": 4.8, "power": 28.0, "status": "WARNING", "health": 74},
    {"id": "M-103", "name": "Exhaust Fan C", "temp": 45.1, "vibration": 0.5, "power": 4.2, "status": "HEALTHY", "health": 99},
    {"id": "M-104", "name": "Compressor Unit D", "temp": 94.3, "vibration": 6.5, "power": 42.1, "status": "ALERT", "health": 52}
]

@app.route('/')
def index():
    return render_template('dashboard.html', machines=machines_db)

@app.route('/api/telemetry')
def telemetry():
    # Simulate slight real-time fluctuations for realism
    for m in machines_db:
        if m['id'] == 'M-104':
            m['temp'] = round(random.uniform(92.0, 96.5), 1)
            m['vibration'] = round(random.uniform(6.2, 6.8), 2)
        elif m['id'] == 'M-102':
            m['temp'] = round(random.uniform(86.0, 90.0), 1)
            m['vibration'] = round(random.uniform(4.5, 5.1), 2)
        else:
            m['temp'] = round(random.uniform(42.0, 76.0), 1)
            m['vibration'] = round(random.uniform(0.4, 1.5), 2)
    
    
    for m in machines_db:
        m['status'] = calculate_status(
            m['temp'],
            m['vibration']
        )

        m['health'] = calculate_health(
            m['temp'],
            m['vibration']
        )

    return jsonify(machines_db)

def calculate_health(temp, vibration):
    temp_penalty = max(0, temp - 40) * 0.5
    vibration_penalty = max(0, vibration - 0.5) * 5

    health = 100 - temp_penalty - vibration_penalty

    return round(max(0, min(100, health)))

def calculate_health(temp, vibration):
    temp_penalty = max(0, temp - 40) * 0.5
    vibration_penalty = max(0, vibration - 0.5) * 5

    health = 100 - temp_penalty - vibration_penalty

    return round(max(0, min(100, health)))


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)

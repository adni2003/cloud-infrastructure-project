from flask import Flask, render_template, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Simulating data that a Cloud Engineer would monitor
    services = [
        {"name": "Database", "status": "Online", "latency": "12ms"},
        {"name": "Storage (S3)", "status": "Online", "latency": "5ms"},
        {"name": "Auth Service", "status": "Warning", "latency": "250ms"}
    ]
    
    return render_template('index.html', 
                           services=services, 
                           updated_at=datetime.datetime.now().strftime("%H:%M:%S"),
                           env=os.environ.get('ENVIRONMENT', 'Production'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
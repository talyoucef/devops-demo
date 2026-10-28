import os
import time
from flask import Flask, jsonify, render_template_string, request, g
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
START_TIME = time.time()

# Prometheus metrics setup
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests",
    ["method", "endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - g.start_time
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.path).observe(latency)
    return response

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Monitoring Demo</title>
    <style>
        body { font-family: system-ui, sans-serif; background: #121212; color: #e0e0e0; padding: 2rem; max-width: 800px; margin: 0 auto; }
        .card { background: #1e1e1e; border: 1px solid #333; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
        h1, h2 { color: #ffffff; }
        a { color: #60a5fa; text-decoration: none; margin-right: 1rem; }
        a:hover { text-decoration: underline; }
        .endpoint { font-family: monospace; background: #2d2d2d; padding: 0.2rem 0.5rem; border-radius: 4px; }
        ul { line-height: 1.8; }
    </style>
</head>
<body>
    <h1>DevOps Monitoring Demo</h1>
    <p>Flask application containerized with Docker and scraped by Prometheus.</p>

    <div class="grid">
        <div class="card">
            <h3>System Info</h3>
            <p><strong>Uptime:</strong> {{ uptime }}s</p>
            <p><strong>Hostname:</strong> {{ hostname }}</p>
            <p><strong>Environment:</strong> {{ env }}</p>
        </div>
        
        <div class="card">
            <h3>Quick Links</h3>
            <p><a href="http://localhost:3000" target="_blank">Grafana Dashboard</a></p>
            <p><a href="http://localhost:9090" target="_blank">Prometheus</a></p>
            <p><a href="/metrics" target="_blank">Raw Metrics</a></p>
            <p><a href="/health" target="_blank">Health Check</a></p>
        </div>
    </div>

    <div class="card">
        <h2>API Routes</h2>
        <ul>
            <li><span class="endpoint">GET /</span> - This dashboard</li>
            <li><span class="endpoint">GET /api/data</span> - Sample JSON response</li>
            <li><span class="endpoint">GET /health</span> - Service health status</li>
            <li><span class="endpoint">GET /metrics</span> - Prometheus exposition</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    uptime = int(time.time() - START_TIME)
    hostname = os.environ.get("HOSTNAME", "unknown")[:12]
    env = os.environ.get("FLASK_ENV", "development")
    return render_template_string(INDEX_HTML, uptime=uptime, hostname=hostname, env=env)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "uptime_seconds": int(time.time() - START_TIME)}), 200

@app.route("/api/data")
def data():
    return jsonify({"items": ["docker", "prometheus", "grafana", "cadvisor"], "count": 4})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
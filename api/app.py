from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Total HTTP Request Count')

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    REQUEST_COUNT.inc()
    response = {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": dict(request.headers),
        "method": request.method,
        "body": request.get_json() if request.is_json else request.get_data().decode()
    }
    return jsonify(response)

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    # Start Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)

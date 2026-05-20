from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Dockerized Microservice!",
        "host": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

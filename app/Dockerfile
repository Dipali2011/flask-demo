# Simple Dockerfile for Flask Application (Without Gunicorn)

FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create non-root user for security
RUN useradd -m appuser

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 5000

# Set environment variables
ENV ENV=production
ENV APP_VERSION=1.0.0

# Start Flask application
CMD ["python", "app.py"]

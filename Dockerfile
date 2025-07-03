# Use Python 3.10.10 base image
FROM python:3.10.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for Pillow, Torch, etc.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg-dev \
        zlib1g-dev \
        git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file first (leverages Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Set environment variables to prevent .pyc files and enable stdout/stderr logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Command to start Flask app
# Flask will auto-detect app.py
CMD ["python", "app.py"]

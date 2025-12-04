# Experiment Container
# Customize for your specific experiment needs

FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy experiment code
COPY . .

# Run experiment
CMD ["python", "run.py"]

FROM python:3.9-slim

WORKDIR /app

# Install dependencies globally (no --user)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV PATH="/root/.local/bin:$PATH"

# Expose ports
EXPOSE 5000
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]


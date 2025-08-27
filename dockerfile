# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (for Django runserver / gunicorn)
EXPOSE 8000

# Run the app
CMD ["python", "main/manage.py", "runserver", "0.0.0.0:8000"]

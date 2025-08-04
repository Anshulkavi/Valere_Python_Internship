# Use official Python image
FROM python:3.11.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files
COPY . . 
COPY .env .

# Expose port 8000
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
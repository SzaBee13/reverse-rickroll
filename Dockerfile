# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy bot files to the container
COPY . .

# Install pip dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional - better with .env bind mount)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]

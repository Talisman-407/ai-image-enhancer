# Use a lightweight Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8090

# Start FastAPI with Uvicorn in a lightweight way
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]


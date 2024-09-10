# Use a slim Python 3.9 image
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . /app

# Expose the application port
EXPOSE 8000

# Run the application using uvicorn, ensuring it is executed as a module

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
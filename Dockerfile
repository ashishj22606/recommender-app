# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Define environment variable
ENV ENV_FILE .env

# Command to run the application
CMD ["python", "/app/src/main.py"]

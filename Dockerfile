# Use the official Python image from the Docker Hub
FROM python:3.9-slim as base

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Test stage
FROM base as test
# Run tests
RUN pytest

# Final stage
FROM base as final
# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=run.py
# Set Flask to production mode
ENV FLASK_ENV=production


# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--timeout", "180", "run:app"]
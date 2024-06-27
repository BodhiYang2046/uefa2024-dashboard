# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Define the entrypoint to be bash
ENTRYPOINT ["/bin/bash", "-c"]
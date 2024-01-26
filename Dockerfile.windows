# Use an official Python runtime as a parent image
FROM python:3.9-windowsservercore

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt with extra index
RUN powershell -Command $ErrorActionPreference = 'Stop'; \
    $ProgressPreference = 'SilentlyContinue'; \
    pip install --no-cache-dir -r requirements.txt --extra-index-url=https://pypi.org/simple/

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME StreamlitApp

# Run ROLE_ADD.py when the container launches
CMD ["python", "ROLE_ADD.py"]

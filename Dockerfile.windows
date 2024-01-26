# Use Windows Server Core 2019 as the base image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set the working directory to /app
WORKDIR /app

# Copy all files from the local root directory to the container at /app
COPY . /app/


# Install Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the local src directory to the container at /app
#COPY src /app

# Copy the requirements.txt file into the container at /app
#COPY requirements.txt /app/

# Copy the installed Python libraries from your local machine
#COPY Lib/site-packages /app/Lib/site-packages

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
#ENV NAME World

# Command to run your application
CMD ["streamlit", "run", "ROLE_ADD.py"]


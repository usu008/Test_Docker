# Use an appropriate Windows base image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set the working directory in the container
RUN mkdir C:\app
WORKDIR C:\app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy your code to the container
COPY . .

# Specify the command to run when the container starts
# CMD ["python", "your_script.py"]
CMD ["python", "ROLE_ADD.py"]

# Use a base image with the desired Python version
FROM python:3.9

# Set the working directory in the container
RUN mkdir /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy your code to the container
COPY . .

# Specify the command to run when the container starts
#CMD ["stream", "your_script.py"]

CMD streamlit run .\new_dashboard.py

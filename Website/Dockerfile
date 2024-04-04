FROM python:3

# Set the working directory

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8001

CMD ["python3", "main.py"]

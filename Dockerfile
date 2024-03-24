# Use the official Python image as a base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code/Travans

# Install dependencies
COPY requirements.txt /code/Travans/
RUN pip install -r requirements.txt

# Copy the current directory into the container at /code/Travans
COPY . /code/Travans/

# Copy the .env file into the container
COPY .env /code/Travans/.env


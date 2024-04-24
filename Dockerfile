FROM python:3.11.9-alpine 

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies including 'make'
RUN apk update && apk add --no-cache gcc libc-dev make

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

EXPOSE 8000

CMD make migrate && make run

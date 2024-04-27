FROM python:3.11.9-alpine 

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies including 'make'

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

EXPOSE 80

CMD poetry run python -m src.manage collectstatic --noinput && poetry run gunicorn -b 0.0.0.0:80 src.project.wsgi

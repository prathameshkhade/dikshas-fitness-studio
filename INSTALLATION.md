# Installation Guide

Follow these steps to set up and run the Diksha's Fitness Studio project on your local machine or using Docker.

## Prerequisites

1. **Python**: Ensure Python 3.11 is installed. You can download it from [python.org](https://www.python.org/).
2. **Poetry**: Install Poetry for dependency management. Run:
   
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```
3. **Docker**: Install Docker from [docker.com](https://www.docker.com/).

## Installation and Setup (Local Machine)

### Step 1: Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/prathameshkhade/dikshas-fitness-studio.git
cd dikshas-fitness-studio
```

### Step 2: Install Dependencies
Use Poetry to install the dependencies:
```bash
poetry install --no-root
```

### Step 3: Configure the Project
1. Set up a `.env` file for environment variables (if required by Django settings).
2. Ensure database configurations in `src/project/settings.py` are correctly set up for your environment.

### Step 4: Run Database Migrations
Apply database migrations:
```bash
poetry run python src/manage.py migrate
```

### Step 5: Collect Static Files
Collect static files for the project:
```bash
poetry run python src/manage.py collectstatic --noinput
```

### Step 6: Run the Development Server
Start the Django development server:
```bash
poetry run python src/manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the application.

## Running the Project with Docker

### Step 1: Build the Docker Image
Build the Docker image using the provided `Dockerfile`:
```bash
docker build -t dikshas-fitness-studio .
```

### Step 2: Run the Docker Container
Run the container:
```bash
docker run -p 80:80 dikshas-fitness-studio
```

The application will now be accessible at [http://127.0.0.1](http://127.0.0.1).


## Additional Commands

### Run Tests
To run tests, use:
```bash
poetry run python src/manage.py test
```

### Create a Superuser
To access the Django admin panel, create a superuser:
```bash
poetry run python src/manage.py createsuperuser
```

For any issues, please refer to the project documentation or raise an issue on the [GitHub repository](https://github.com/prathameshkhade/dikshas-fitness-studio).

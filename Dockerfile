# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=django_task_api_project.settings

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Create database (assuming you're using PostgreSQL)
RUN service postgresql start && \
    su - postgres -c "psql -c 'CREATE DATABASE global_task_api;'" && \
    su - postgres -c "psql -c \"CREATE USER global_task_user WITH PASSWORD 'global_task_password';\"" && \
    su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE global_task_api TO global_task_user;'"

# Run migrations
RUN python manage.py migrate

# Expose the port django is running on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

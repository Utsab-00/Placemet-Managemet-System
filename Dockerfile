# Use a Python base image (Debian-based is common)
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install MariaDB client libraries (for the container's OS)
RUN apt-get update && \
    apt-get install -y libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
#update pip vertion
RUN pip install --upgrade pip

# Copy the entire project into the container
COPY . .

# Set environment variables (if needed, e.g., for Django settings)
# ENV DJANGO_SETTINGS_MODULE=my_project.settings

# Expose the port your Django development server runs on (default is 8000)
EXPOSE 8000

# Command to run your Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

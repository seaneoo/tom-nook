# Use Python 3.11.4 for the production environment
FROM python:3.11.4-alpine3.18

# Ensure Make is installed
RUN apk update && apk add --no-cache make

# Set the working directory
WORKDIR /bot

# Install Pipenv
RUN pip install pipenv

# Copy the required files for installation from the project directory
COPY Pipfile .
COPY Pipfile.lock .
COPY .env .
COPY Makefile .

# Set up the production environment
RUN pipenv sync

# Define the location of the virtual environment
ENV PATH="/.venv/bin:$PATH"

# Copy the rest of the project files
COPY . .

# Run the application
CMD [ "make", "run" ]

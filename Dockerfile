FROM python:latest

# Expose the app port.
EXPOSE 8000

# Install pipenv
RUN pip install pipenv

# Copy over source code
COPY . .

# Install dependencies
RUN pipenv install

# Run the app
CMD pipenv run serve --host 0.0.0.0

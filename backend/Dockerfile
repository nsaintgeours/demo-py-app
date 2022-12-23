# Install Python
FROM python:3.9

# Copy and install requirements
COPY requirements.txt /
RUN pip install -r ./requirements.txt

# Copy and install project sources
COPY setup.py /
COPY MANIFEST.in /
COPY src /src
RUN pip install .

# Set port on which the API is served
# either 8088, or a custom port passed as an environment variable named BACKEND_PORT in the build command
ARG BACKEND_PORT=8088
EXPOSE ${BACKEND_PORT}

# Launch REST API
CMD uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT

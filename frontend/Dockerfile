# Install Python
FROM python:3.9

# Copy and install requirements
COPY requirements.txt /
RUN pip install -r ./requirements.txt

# Copy and install project sources
COPY setup.py /
COPY ../src ./src
RUN pip install .

# Set port on which the web app' is served:
# either 8501, or a custom port passed as an environment variable named WEBAPP_PORT in the build command
ARG WEBAPP_PORT=8501
EXPOSE ${WEBAPP_PORT}
ENV STREAMLIT_SERVER_PORT ${WEBAPP_PORT}

# Run Streamlit web app'
CMD ["streamlit", "run", "src/frontend/app.py"]
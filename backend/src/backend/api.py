"""
Starts the REST API service and defines API endpoints
"""

import json
import logging
import os
from pathlib import Path
from typing import Optional, List

from backend.dataclasses import InputData, OutputData, User, Measurement
from backend.db_client import DbClient
from backend.engine import Engine
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Query

# Load default parameters from .env file
load_dotenv(dotenv_path=Path(__file__).parent.parent.parent.parent / '.env')

# Set log level
logging.basicConfig(level=os.getenv('LOG_LEVEL'))

# Create data processing engine
engine = Engine()

# Connect to database
db_client = DbClient()

# Start REST API service
app = FastAPI(
    title="REST API for the Demo Py app backend",
    description="A very basic REST API implemented with Python and FastAPI library",
    version="0.0.1",
    contact={"name": "Nathalie Saint-Geours", "email": "nathalie.saint-geours@m4x.org"},
    license_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0.html"}
)

# Load example data
sample_json = Path(__file__).parent / 'resources' / 'sample_input_data.json'
with open(sample_json) as file:
    sample_data = json.load(file)


# REST API endpoint to fetch users from the MySQL database
@app.get('/api/v0/fetch_users', response_model=List[User], tags=["My REST API"])
def fetch_users() -> List[User]:
    return db_client.fetch_users()


# REST API endpoint to fetch user measurements from the MySQL database
@app.get('/api/v0/fetch_user_measurements', response_model=List[Measurement], tags=["My REST API"])
def fetch_user_measurements(user_id: int = Query(description='User ID')) -> List[Measurement]:
    return db_client.fetch_user_measurements(user_id=user_id)


# REST API endpoint to process data with the data processing engine
@app.post('/api/v0/process', response_model=OutputData, tags=["My REST API"])
def process(
        data: InputData =
        Body(..., description='Input data passed as request JSON body.', example=sample_data),

        some_param: Optional[float] =
        Query(description='Some data processing parameter', ge=0, le=1, default=0.0),

) -> OutputData:
    query_params = locals()
    data = query_params.pop('data')
    return engine.run(data=data, **query_params)

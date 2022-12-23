# DemoPyApp

A simple web app' with a database / backend / frontend architecture, using:

- a MySQL database
- a Python backend which exposes a REST API implemented with `fastapi` and `pydantic`
- a Python frontend based on [Streamlit]()

## Table of contents

[1. Usage with Docker](#1-usage-with-Docker)  
[2. Usage (development mode)](#2-usage-(development-mode))

* [2. Usage (development mode)](#2-usage-(development-mode))

## 1. Usage with Docker

**Prerequisites**

- Docker and Docker Compose installed on your computer
- Docker Desktop is launched (on Windows)

**Steps**

- open a terminal, and **move to the project's root folder**:

```sh
> cd demo-py-app
```

- launch the web app':

```bash
docker compose up -d --build
```

- open the web app on your internet browser at [`http://localhost:8504`](http://localhost:8504).

*Details*: the `docker compose up` command starts three services that are defined in the `docker-compose.yml` file,
using environment variables defined in the `.env` file. The first service is a MySQL database populated with some sample
data. The second service is the application backend, served through a REST API. The third service is the application
frontend, e.g., a simple web app'. The `--build` option forces Docker to build the backend and frontend Docker images
from source code.

## 2. Usage (development mode)

**Prerequisites**

- Docker and Docker Compose installed on your computer
- Docker Desktop is launched (on Windows)
- `python==3.9` and `pip` are installed on your computer

**Steps**  
To run the demo web app' in development mode, you need to follow these steps:

- install a dedicated Python virtual environment
- start database service with with `docker-compose`
- start the application backend
- start the application frontend

We describe these four steps below.

### 2.1. Installation

- open a terminal, and **move to the project's root folder**:

```sh
> cd demo-py-app
```

- create and activate a virtual environment for the project:

```sh
python -m venv myenv
myenv\Scripts\activate
```

- make sure you have the latest versions of `pip` and `setuptools` libraries installed:

```sh
pip install --upgrade pip
pip install --upgrade setuptools
```

- install the application backend:

```sh
pip install -e ./backend/src
```

- install the application frontend:

```sh
pip install -e ./frontend/src
```

## 2.2. Start database service

We use `docker compose` to start the database service.

```bash
docker compose up -d database
```

This command starts the `database` service which is defined in the `docker-compose.yml` file, using environment
variables that are listed in the `.env` file.

### 2.3. Start application backend

We can now start the application backend, with a REST API exposed on local host on port 8088, with:

```bash
uvicorn backend.api:app --host 0.0.0.0 --port 8088
```

### 2.4. Start application frontend

We can now start the application front on local host on port 8501 with:

```bash
streamlit run frontend/src/frontend/app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.12:8501
```

You can open the web app on your internet browser at [`http://localhost:8501`](http://localhost:8501).

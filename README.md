# Linux Command Executor API

A secure Linux Command Executor API built using Python and FastAPI. This project executes predefined Linux commands and returns system information in JSON format.

## Project Overview

The purpose of this project is to create a secure FastAPI-based API that runs only predefined Linux system commands. Dynamic/custom command execution is not allowed for security reasons.

## Features

* System uptime information
* Disk usage details
* Memory usage details
* Current logged-in user
* Health check endpoint
* JSON formatted responses
* Error handling using Python subprocess module
* Secure predefined command execution

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Linux Commands
* Git & GitHub

## Project Structure

```text
project/
│
├── main.py
├── routes/
├── utils/
├── requirements.txt
└── README.md
```

## API Endpoints

### 1. Health Check

**Endpoint:**

```http
GET /health
```

**Response:**

```json
{
  "status": "healthy"
}
```

---

### 2. System Uptime

**Endpoint:**

```http
GET /system/uptime
```

**Linux Command Used:**

```bash
uptime
```

---

### 3. Disk Usage

**Endpoint:**

```http
GET /system/disk
```

**Linux Command Used:**

```bash
df -h
```

---

### 4. Memory Usage

**Endpoint:**

```http
GET /system/memory
```

**Linux Command Used:**

```bash
free -m
```

---

### 5. Current User

**Endpoint:**

```http
GET /system/user
```

**Linux Command Used:**

```bash
whoami
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/linux-command-executor-api.git
```

Move into the project directory:

```bash
cd linux-command-executor-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Requirements

Example `requirements.txt`

```txt
fastapi
uvicorn
```

## Security Note

This API only allows predefined Linux commands:

* uptime
* df -h
* free -m
* whoami

Custom command execution is disabled for security purposes.



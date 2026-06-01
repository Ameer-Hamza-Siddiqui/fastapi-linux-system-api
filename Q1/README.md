# Linux Command Executor API

## Project Overview

This project is a basic Linux Command Executor API built using Python and FastAPI.  
It executes only predefined Linux system commands and returns their output in JSON format.

For security reasons, users are not allowed to execute custom commands.

## Features

- FastAPI-based REST API
- Executes predefined Linux commands only
- Proper JSON responses
- Error handling
- Health check endpoint
- Secure command execution using Python subprocess module

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/system/uptime` | Get system uptime |
| GET | `/system/disk` | Get disk usage using `df -h` |
| GET | `/system/memory` | Get memory usage using `free -m` |
| GET | `/system/user` | Get current logged-in user |

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Linux Commands
- Git
- GitHub

## Installation

```bash
git clone YOUR_GITHUB_REPO_LINK
cd linux-command-executor-api
pip install -r requirements.txt
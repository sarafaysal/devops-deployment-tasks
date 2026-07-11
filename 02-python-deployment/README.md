# Python Application Deployment

## Objective
Deploy a Python Flask application using Gunicorn and Nginx.

## Technologies Used
- Ubuntu 24.04 (WSL2)
- Python 3.12
- Flask
- Gunicorn
- Nginx

## Architecture

Browser
↓
Nginx
↓
Gunicorn
↓
Flask Application

## Commands Used

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Install Packages

```bash
pip install flask gunicorn
```

Run Gunicorn

```bash
gunicorn --bind 127.0.0.1:8000 app:app
```

Test Nginx

```bash
sudo nginx -t
```

Restart Nginx

```bash
sudo service nginx restart
```

## Result

Successfully deployed the Flask application using Nginx as a reverse proxy.

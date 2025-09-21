# ALX Travel App

A real-world Django application that serves as the foundation for a travel listing platform. This project demonstrates a scalable backend setup, MySQL integration, REST API development, and Swagger-based API documentation.

---

## Project Structure

alx_travel_app/ <- Parent folder / GitHub repo root
├── manage.py <- Django management script
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── alx_travel_app/ <- Django project folder
├── init.py
├── settings.py
├── urls.py
├── wsgi.py
├── asgi.py
└── listings/ <- Core app folder
├── init.py
├── admin.py
├── apps.py
├── models.py
├── urls.py
└── views.py

yaml
Copy code

---

## Features

- Modular Django project setup for scalability
- MySQL database integration using `django-environ` for secure credentials
- RESTful API using Django REST Framework
- CORS support with `django-cors-headers`
- Automated API documentation via Swagger (`drf-yasg`)
- Prepared for asynchronous tasks with Celery

---

## Prerequisites

- Python 3.10+  
- Virtual environment (`venv` or `virtualenv`)  
- MySQL server installed and running  

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/alx_travel_app.git
cd alx_travel_app
Create and activate virtual environment

bash
Copy code
python -m venv tutorial-env
tutorial-env\Scripts\activate   # Windows
# source tutorial-env/bin/activate  # macOS/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
Configure environment variables

Create a .env file in the root folder with the following example:

env
Copy code
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
Run database migrations

bash
Copy code
python manage.py migrate
Run the development server

bash
Copy code
python manage.py runserver
Swagger docs: http://127.0.0.1:8000/swagger/

Test API: http://127.0.0.1:8000/api/listings/hello/

Usage
Add new travel listings in the listings app

Extend APIs with Django REST Framework serializers and views

Configure Celery for background tasks in future milestones

Contributing
Fork the repository

Create a feature branch (git checkout -b feature-name)

Commit changes (git commit -m "Add feature")

Push branch (git push origin feature-name)

Open a pull request

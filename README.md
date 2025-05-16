# Remind-me-later Django REST API

This project implements a simple Django REST API that sends and logs email reminders. It supports scheduling reminders via email and saving them to a PostgreSQL database.

## 🔧 Features

- Send email reminders using a POST API request.
- Logs all sent email reminders into the PostgreSQL database.
- Structured for scalability using Django apps and modular file separation.

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- SMTP Email (Gmail)

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/dipti-biswas-ship-it/Remind_Me_Later.git
    cd remind-me-later
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure PostgreSQL database in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Configure SMTP email settings in `settings.py`:
    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your_email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your_app_password'
    ```

6. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Run the server:
    ```bash
    python manage.py runserver
    ```

## API Endpoint

- POST `/api/reminders/send-email/`  
  Send an email and log it.

### Request Body

```json
{
  "to_email": "recipient@gmail.com",
  "subject": "Meeting Reminder",
  "message": "Don't forget about the meeting at 10 AM tomorrow."
}
# School Management System

A simple Django project to manage school information.

## Prerequisites

- Python 3.8+
- pip
- Virtual environment tool (`venv` or `virtualenv`)
- PostgreSQL

## Setup Instructions

1. **Clone the Repository**:

```bash

   git clone https://github.com/Springhawk27/django_project.git

```

2. **Create and Activate Virtual Environment**:

```bash

   python -m venv venv
   cd .\django_project
   source  venv\Scripts\activate

```

3. **Install Dependencies**:

```bash

   pip install -r requirements.txt

```

5. **Apply Migrations**:

```bash

   python manage.py makemigrations
   python manage.py migrate

```

6. **Run the Server**:

```bash

   python manage.py runserver

```

Visit http://127.0.0.1:8000 in your browser.

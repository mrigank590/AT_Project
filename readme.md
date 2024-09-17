# Notes App

A simple Django application for managing notes with user authentication and JWT-based session management.

## Features

- User registration and login
- JWT authentication
- CRUD operations for notes
- PostgreSQL setup (before Dockerizing)

## Prerequisites

- Python 3.x
- PostgreSQL
- psycopg2-binary

## Step-by-Step Guide for Testing with PostgreSQL

### Step 1: Install PostgreSQL and psycopg2

1. **Install PostgreSQL:**
   Download and install PostgreSQL from the official website: [PostgreSQL Download](https://www.postgresql.org/download/)

2. **Install psycopg2:**
   Install the PostgreSQL adapter for Python:

   ```bash
   pip install psycopg2-binary
   ```

### Step 2: Configure Django to Use PostgreSQL

1. **Update Database Settings:**
   Edit the `DATABASES` section in `settings.py` to use PostgreSQL:

   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "notes_db",
           "USER": "your_postgres_user",
           "PASSWORD": "your_postgres_password",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }
   ```

### Step 3: Apply Migrations

1. **Make Migrations:**

   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

### Step 4: Run the Development Server

1. **Create a Superuser (Optional):**

   ```bash
   python manage.py createsuperuser
   ```

2. **Run the Server:**

   ```bash
   python manage.py runserver
   ```

### Step 5: Test the Endpoints

You can use Postman or a similar API testing tool to test the following endpoints:

1. **Register a New User:**

   Send a `POST` request to `http://127.0.0.1:8000/api/register/` with the following JSON body:

   ```json
   {
       "username": "testuser",
       "password": "testpassword"
   }
   ```

2. **Log In to Obtain JWT Tokens:**

   Send a `POST` request to `http://127.0.0.1:8000/api/login/` with the following JSON body:

   ```json
   {
       "username": "testuser",
       "password": "testpassword"
   }
   ```

3. **Create a New Note:**

   Send a `POST` request to `http://127.0.0.1:8000/api/notes/` with the following JSON body and the JWT token in the Authorization header:

   ```json
   {
       "title": "Sample Note",
       "content": "This is a sample note."
   }
   ```

4. **Retrieve All Notes:**

   Send a `GET` request to `http://127.0.0.1:8000/api/notes/` with the JWT token in the Authorization header.

5. **Update an Existing Note:**

   Send a `PUT` request to `http://127.0.0.1:8000/api/notes/<id>/` with the following JSON body and the JWT token in the Authorization header:

   ```json
   {
       "title": "Updated Note",
       "content": "This is an updated note."
   }
   ```

6. **Delete a Note:**

   Send a `DELETE` request to `http://127.0.0.1:8000/api/notes/<id>/` with the JWT token in the Authorization header.

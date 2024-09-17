
# Notes App

A simple Django application for managing notes with user authentication and JWT-based session management.

## Features

- User registration and login
- JWT authentication
- CRUD operations for notes
- Dockerized setup with PostgreSQL

## Prerequisites

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mrigank590/AT_Project.git
cd notes-app
```

### 2. Build and Run the Docker Containers

```bash
docker-compose up --build
```

### 3. Apply Migrations

Open a new terminal window and run the following command to apply the database migrations:

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser (Optional)

If you want to create a superuser for accessing the Django admin interface, run the following command:

```bash
docker-compose exec web python manage.py createsuperuser
```

## API Endpoints

### User Registration

- **Endpoint:** `POST /api/register/`
- **Body:**
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }
  ```

### User Login

- **Endpoint:** `POST /api/token/`
- **Body:**
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }
  ```
- **Response:**
  ```json
  {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }
  ```

### Create Note

- **Endpoint:** `POST /api/notes/`
- **Headers:**
  ```json
  {
    "Authorization": "Bearer your_access_token"
  }
  ```
- **Body:**
  ```json
  {
    "title": "New Note",
    "content": "This is a new note."
  }
  ```

### View Notes

- **Endpoint:** `GET /api/notes/`
- **Headers:**
  ```json
  {
    "Authorization": "Bearer your_access_token"
  }
  ```

### Update Note

- **Endpoint:** `PUT /api/notes/<int:pk>/`
- **Headers:**
  ```json
  {
    "Authorization": "Bearer your_access_token"
  }
  ```
- **Body:**
  ```json
  {
    "title": "Updated Note",
    "content": "This is an updated note."
  }
  ```

### Delete Note

- **Endpoint:** `DELETE /api/notes/<int:pk>/`
- **Headers:**
  ```json
  {
    "Authorization": "Bearer your_access_token"
  }
  ```

# MyCart API

MyCart is a Django REST API project designed to manage blog posts and user authentication. It provides endpoints to create, read, update, and delete posts, along with user registration and JWT-based authentication including token blacklisting for secure logout.

## Features

- **Post Management**  
  - Create, retrieve, update, and delete blog posts  
  - Posts are categorized and can have images uploaded  
  - Search posts by slug  

- **User Management**  
  - Custom user model with email as the username field  
  - User registration endpoint  
  - Password hashing and validation  
  - JWT authentication with access and refresh tokens  
  - Token blacklisting for logout  

## Tech Stack

- Python 3.x  
- Django 5.0  
- Django REST Framework  
- Simple JWT for authentication  
- SQLite (default database)  

## Project Structure Highlights

- `fresh` app: Handles blog post models, serializers, and views  
- `users` app: Custom user model, registration serializers, and authentication views  
- Uses environment variables for sensitive settings (e.g., `DJANGO_SECRET_KEY`)  
- Supports image uploads for posts  

## Getting Started

### Prerequisites

- Python 3.x  
- Virtual environment tool (recommended: `venv` or `virtualenv`)  

### Installation

### 1. Clone the repo:  
```bash
   git clone https://github.com/DanielAboagye233/Django-Api.git
   cd MyCart
```

### 2. Create and activate a virtual environment:
```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies:
```bash
    pip install -r requirements.txt
```

### 4. Create a .env file in the project root and add your environment variables:
```bash
    DJANGO_SECRET_KEY=your_secret_key_here
    DJANGO_DEBUG=True
```

### 5. Apply migrations:
```bash
    python manage.py migrate
```

### 6. Run the development server:
```bash
    python manage.py runserver
```

## API Endpoints Overview

### Posts
- **List posts**: `GET /api/posts/`
- **Retrieve post by slug**: `GET /api/posts/{slug}/`
- **Create post**: `POST /api/posts/`
- **Update post**: `PUT /api/posts/{id}/`
- **Delete post**: `DELETE /api/posts/{id}/`
- **Search posts**: `GET /api/posts/search/`

### User Registration
- **Register new user**: `POST /api/user/register/`

### Authentication
- **Obtain JWT tokens**: `POST /api/token/`
- **Refresh JWT token**: `POST /api/token/refresh/`
- **Logout (token blacklist)**: `POST /api/user/logout/`

- Updated API Endpoints section in README.md


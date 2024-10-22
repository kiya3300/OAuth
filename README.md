# Project Name

Brief description of your project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Project repository:


`[Mereb auth] ... ` 

2. Navigate to the project directory:

```
cd django-assesment
```
3. Create and activate a virtual environment:

``` 
python -m venv venv
```
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Unix/MacOS:

  ```
  source venv/bin/activate
  ```
4. Install dependencies from `requirements.txt`:
```
pip install -r requirements.txt
```

## Usage

1. Run migrations to set up the database:
```
python manage.py migrate
```
2. Create a superuser for accessing the Django admin:
```
python manage.py createsuperuser
```
3. Start the development server:
```
python manage.py runserver
```
4. Access the admin interface at `http://localhost:8000/admin/` to manage users and profiles.

## API Endpoints

- `POST /api/signup/`: Register a new user.
- `POST /api/login/`: Login with username and password.
- `POST /api/logout/`: Logout the authenticated user.
- `POST /api/password-reset/`: Request a password reset.
- `POST /api/password-reset-confirm/<uidb64>/<token>/`: Confirm a password reset.
- `GET /api/profiles/`: List all profiles.
- `GET /api/profiles/<id>/`: Retrieve a specific profile.
- `POST /api/profiles/`: Create a new profile.
- `PUT /api/profiles/<id>/`: Update an existing profile.
- `DELETE /api/profiles/<id>/`: Delete a profile.
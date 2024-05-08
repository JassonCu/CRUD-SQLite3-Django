# CRUD-Django-Extended

Complete CRUD application built with Python, Django, and a SQLite3 database. This project utilizes the MTV architecture pattern (Model - Template - View), the Django ORM, the CSS Bootstrap framework, and JavaScript for event handling.

## Changes Overview

The project has been extended to include additional features and modules to enhance its functionality and professionalism. Major updates include:

- Integration of new modules: 'courses', 'students', 'teachers', 'communication', 'grade', and 'reports'.
- Upgrade to Django version 5.0.6 for compatibility with latest features and security patches.

## Screenshots

![Captura](https://user-images.githubusercontent.com/85533418/147376300-0663b086-ca02-4a47-9508-4396c1f44dbc.PNG)
_Edit Course Form:_
![EditForm](https://user-images.githubusercontent.com/85533418/147376312-b8e5eab3-96ee-478d-b79e-81fe7d5b5ef4.PNG)

## Instructions

To run the program, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/JassonCu/CRUD-SQLite3-Django.git
   ```

2. Create a Virtual Enviroment
    ```
    python -m venv env
    ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations
    ```
    python manage.py migrate
    ```

5. Run the Django server:
   ```
   python manage.py runserver
   ```

## Reverting to Previous Versions

If you prefer to use the project without the recent updates, you can revert to previous commits by using Git.

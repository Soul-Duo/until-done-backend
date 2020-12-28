# Until Done Backend API Server

## Requirements

- Python
- vscode (prettier extension installed)

## Installation

1. Install and create virtualenv

   ```shell
   $ pip install virtualenv     # Install virtualenv
   $ virtualenv venv            # Create virtual environment for the project
   ```

2. Activate virtualenv

   - Windows
     ```shell
     $ ./venv/Scripts/activate    # Activate the virtual environment
     ```
   - Linux / macOS

     ```shell
     $ source ./venv/bin/activate # Activate the virtual environment
     ```

3. Install requirements on virtualenv

   ```shell
   (venv)$ pip install -r requirements.txt # Install required packages for the project
   ```

## Project Setup

1. You need to create a superuser for admin access.

   ```shell
   (venv)$ python manage.py createsuperuser --email [your-email] --password [your-password] # Create admin
   ```

2. Make migrations and migrate for database.

   ```shell
   (venv)$ python manage.py makemigrations
   (venv)$ python manage.py migrate
   ```

## Run server

```shell
$ python manage.py runserver [port]
```

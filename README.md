# Quiz Application with Flask

Deployed at [Quiz Websitesine Hoşgeldiniz! - FlaskApp](https://dagbfatih.pythonanywhere.com/).

Developed by **Beşir Fatih Dağ**.

Hi, this project is developed with Flask and SQLAlchemy. You can solve pre-added questions in the quiz and see your results. To run the application on your local development environment, please go to `Getting Started` section below. To deploy the project on a hosting server, go to `Deployment` section. Read `Project Structure` section below to understand the structure and logic of the application. Please enjoy surveying!

# Getting Started

To get started, clone or install the project.
Open it in an editor like `Visual Studio Code`.
Open a terminal and come to the `flask_quiz_project/` directory.

# Running Application

Run the application locally and learn some basic codes.

## Requirements

You should be installed `python` and `pip` in your working environment (server or your OS).

## Dependencies

Firstly, create a virtual environment to install required packages locally.

Create a Virtual Environment (venv):
`python -m venv my_env`

Activate in in terminal:
Windows:

```bash
.\my_env\Scripts\activate
```

Ubuntu:

```bash
source my_env/bin/activate
```

Now you are ready to install dependencies.

Run:

```bash
pip install -r requirements.txt
```

This will install the necessary dependencies in `requirements.txt`. Please ensure that all deps are installed successfully.

Now, start the server from the terminal that `venv` is activated in.

Run the server:

```bash
flask --app src/app --debug run
```

Now, you are started your application. Your application is ready to accept API requests and to be visited in client templates.
However, the database is not configured yet. Let's create tables and seed some data to database.

To do this, run commands below:

Run migration:

```bash
flask --app src/app migration:fresh
```

Run seeders:

```bash
flask --app src/app db:seed
```

Now, you are completely ready. Let's visit `http://localhost:5000/` (the port can change according to your local network; you can see the port in terminal logs when you start the application by `flask run` command above).

When you start the application and visit the root (`http://localhost:5000/`), you will be redirected to a login page. Now you need some credentials to test the application.

## Credentials

There are 6 predefined users with same password:
**Usernames:**
`user`
`user2`
`user3`
`user4`
`user5`
`user6`

**Password:**
`12345678`

Try one of them and start solving quizzes.

# Deployment

This project is deployed at [Quiz Websitesine Hoşgeldiniz! - FlaskApp](https://dagbfatih.pythonanywhere.com/).

Before starting, it's good to know that you should be able to access a terminal in hosting server.

Enter the terminal and clone the project with using `git clone`.
Follow the instructions above in `Dependencies` section.

## WSGI Configuration

Find the wsgi config file, in ubuntu it is at somewhere like `/var/www/<your_username>_pythonanywhere_com_wsgi.py`.

Now, do the configuration:

```python
import sys
import os

path = '/home/Dagbfatih/flask_quiz_project'
if path not in sys.path:
    sys.path.insert(0, path)

# Import your Flask app
from src.app import create_app  # Import the create_app function

# Create the app instance by calling the factory function
app = create_app()

# Assign the Flask app to the WSGI application variable
application = app
```

Restart the server.

# Project Structure

# Root Files

In the root of project, you will see there are 2 important files named `config.py` and `requirements.txt` and `src/` directory.

`config.py` file is for storing environment variables.
`requirements.txt` file includes the required packages to run this application.
`src/` directory contains the source codes.

**Let dive in source code structure!**

in `src`, there is `app.py` file that is the main entry point file.
You will see two main directories: `client/` and `server/`. These are for separating user interface and backend side of the application. `server/` directory has api endpoints and services. `client/` has the html templates. In most applications server and client codes consist of 2 separate projects but in this project they are configured as one project. However, to supply maximum abstraction they separated as client and server. But they are dependent and some client blueprint codes use the codebase of server, not the api endpoints.

## Server Side

Firstly, let me explain the folders inside `server/`:

`commands/`: CLI commands that are written to make some things easier.
`configs/`: Some configurations like db, ioc registrations.
`core/seeders/`: Base and independent classes and interfaces.
`database/seeders/`: Database seeders to seed data easily.
`enums/`: Enums.
`models/`: Database models.
`routes/`: Blueprints and routes.
`services/`: Services that manages database operations and logic. Some services used by `client` side codes.

Now dive into some directories.

### Commands

There are currently two commands:

`migration:fresh` -> Drops all tables and creates all again. So, it cleans db.

`db:seed` -> Runs the seeders inside `src/database/seeders/` directory.

### Seeders

Seeders are built for sending predefined users, exams and scores as automatically.

## Client Side

Client side has 3 folders: `services`, `templates` and `routes`.

`services/` -> includes the client services to capsulate some beneficial methods like sorting, finding maximum score for a user.

`templates/` -> includes .html files and structured well.

`routes/` -> includes client blueprints and routes.

Their concepts are similar and easy to understand. Let look at template because it may be a bit complicated.

### Templates

I used Bootstrap 5 in this project as CSS framework.
Templates has 3 directories and 2 file:

`base.html` -> Has only css links and JavaScript bundles from 3d party sources. Wraps all templates.

`components` -> Includes small components such as navbar and footer.
`layouts` -> Wraps pages and all of them extends from `base.html`.
`pages` -> Represents the routing structure, wrapped under a selected `layout`.

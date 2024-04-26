# Welcome to Flask Authentication Web App!
This is a secure and scalable authentication web application built using Flask micro-framework. This app follows best practices in Flask development and includes various features such as Access Control List (ACL), Rate Limiting, Background Jobs, Caching, Logging, Error Handling, Protection from Open Redirects, Session Management, Two Factor Authentication (2FA), and User Email Confirmation, db migrations, etc.

## Features
- Access Control List: The app enforces ACL policies based on user roles and permissions, ensuring proper authorization of resources.

- Rate Limiting: To prevent abuse or brute force attacks, the app implements rate limiting to restrict the number of requests per IP address within a specific time frame.

- Background Jobs: Asynchronous tasks are executed in the background using Celery task queue to ensure responsive user experience while performing long-running operations.

- Caching: Response data is cached to improve performance by reducing database queries and server load. Memcached and Redis are used as cache backends.

- Logging: All activities performed by users and system events are logged with timestamps, user IDs, and other relevant metadata to aid debugging and monitoring.

- Error Handling: Comprehensive error handling mechanisms are implemented to provide informative error messages and graceful degradation during unexpected conditions.

- Protection from Open Redirects: The app prevents unauthorized redirection to external websites to protect against phishing attacks.

- Session Management: Secure and persistent sessions are maintained across multiple pages to maintain user state and preferences.

- User Email Confirmation: Users must confirm their email addresses before activating their accounts to verify ownership and prevent fraudulent registrations.

## Prerequisites
To get started with this project, make sure you have installed the following dependencies:
- Python(3.8 or higher)
- pip
- sqlite, PostgreSQL or MySQL server
- RabbitMQ server
- git

## Architecture
The app uses a modular design approach, separating concerns into smaller modules to promote reusability and maintainability. Here's a high-level overview:

- Application Factory: The app initializes using `create_app()` function in `app/__init__.py` which sets up configuration, extensions, middleware, and blueprints. It allows creating separate instances of the app for testing and production environments.

- Extensions: Various third-party libraries like Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Bcrypt, Flask-Limiter, Flask-Cache, Flask-Sessions, Celery, etc., are integrated into the app as extensions for added functionality.

- Blueprints: Different parts of the app are organized into individual blueprints, each having its own static files, and view functions. Blueprints include auth, admin, users.

- Database Models: Database models representing entities like users, roles, permissions, tokens, logs, and emails are defined in SQLAlchemy ORM classes.

- Context Processors: Global variables needed throughout the app are initialized in context processors and passed along with every request.

- Templates: HTML templates using Jinja2 syntax to render dynamic content and incorporate Bootstrap CSS framework for styling.

- Static Files: Static assets including JavaScript, Jquery, CSS, images, fonts, and favicons are served separately through Nginx or any other HTTP server.

- Configuration: Multiple environment configurations allow customizing settings depending on whether the app runs locally, staging, QA, or production environments.

## Getting Started

- Clone the repository:
```
git clone <repository URL>.
```

- Install `rabbitmq-server` on your machine
```
# on linux
sudo apt install rabbitmq-server -y
```

- Set Up the rabbitMQ server
```
# creates a  rabbitMQ user and Password
sudo rabbitmqctl add_user sammy_d_explorer mypasswordIss!mple

# creates a virtual host in the rabbitMQ Server
sudo rabbitmqctl add_vhost my_app_vhost

# creates rabbitMQ user tag
sudo rabbitmqctl set_user_tags sammy_d_explorer mytag

# giving user permissions to virtual host
sudo rabbitmqctl set_permissions -p my_app_vhost sammy_d_explorer ".*" ".*" ".*"
```

- Create virtualenv:
```
python3 -m venv venv.
```

- Activate virtualenv:
```
# on unix systems
source venv/bin/activate

# On windows
venv\Scripts\activate
```

- Install dependencies:
```
pip install -r requirements.txt.
```

- Configure the app by copying `prod_config.py.example` file to `config/prod_config.py` and editing according to your needs.

- Create a `.env` file and provide values for the following variables needed for the smooth running of our app.
```
APP_SECRET_KEY = "insert your secret key here"
DB_URL = "<Insert db url here>"
SMTP_MAIL = ""
SMTP_PWD = ""
SMTP_HOST = ""
SMTP_PORT = 
USE_SSL = ""
USE_TLS = ""
BROKER_URL = ""
```
> The value for `SMTP_PORT` should be an `Integer` while the values for `USE_TLS` and `USE_TLS` should be boolean value i.e either `True` or `False`

- Run migrations: `flask db init`, then `flask db migrate -m "Initial migration"` and finally `flask db upgrade`.

- Run the app: 
```
# on one terminal run the below command
python3 run.py

# on another run the below command to start celery app
celery -A make_celery worker --loglevel INFO
```

- Visit `<http://localhost:5000>` in your browser.

## Conclusion
Flask Authentication Web App provides robust authentication capabilities combined with scalable architecture, allowing seamless growth and expansion over time. Following established best practices ensures efficient development workflow, reliable operation, and consistent quality.

# Useful Resources
- Flask
    - [flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
    - [flask login](https://flask-login.readthedocs.io/en/latest/)
    - [flask limiter](https://flask-limiter.readthedocs.io/en/stable/)
    - [flask cache](https://flask-caching.readthedocs.io/en/latest/)
    - [flask mail](https://pythonhosted.org/Flask-Mail/)
    - [Background Task with Celery](https://flask.palletsprojects.com/en/3.0.x/patterns/celery/)

- Celery
    - [First steps with celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)
    - [Using rabbitMQ with celery](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq)
    - [RabbitMQ Tutorials](https://www.rabbitmq.com/tutorials)
    - [Installing RabbitMQ](https://www.rabbitmq.com/docs/download)

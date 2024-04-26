from celery import Celery, Task
from flask import Flask
from config.task_queue_config import CeleryDevConfig
from dotenv import load_dotenv
import os


load_dotenv()
def celery_init_app(app: Flask) -> Celery:
    """creates celery app from the flask instance"""

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(
            app.name, 
            task_cls = FlaskTask,
            broker=os.getenv("BROKER_URL"),
            #backend="", # rpc server
        )

    celery_app.config_from_object(CeleryDevConfig)
    celery_app.set_default()
    app.extensions["celery"] = celery_app

    return celery_app

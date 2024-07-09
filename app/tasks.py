from celery import Celery

celery = Celery(__name__)

def init_celery(app):
    celery.conf.update(app.config)
    return celery
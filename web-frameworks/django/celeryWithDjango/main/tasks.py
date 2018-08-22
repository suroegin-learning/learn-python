import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from celeryWithDjango.celery import app


@app.task
def print_verification_address(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        print("http://localhost:8000/verify/{}/".format(
            str(user.verification_uuid)))
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
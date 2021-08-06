from settings import base

import os

from mongoengine import connect, disconnect

DJANGO_SETTINGS_MODULE = 'settings.production'

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

disconnect()

connect(
    'kargodb',
    host='kargo-docdb-2020-11-30-18-20-37.cluster-cdw1z9oml9cr.us-west-2.docdb.amazonaws.com',
    port=27017,
    username='kargo-prod',
    password='##KargoProd#2021##'
)

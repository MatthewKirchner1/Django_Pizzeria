import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from MainApp.models import Pizza, Topping

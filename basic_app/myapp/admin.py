from django.contrib import admin

# Register your models here.

'''
(Optional)
If you want to manage your model through the Django admin interface, you can register it.
'''

from .models import BankAccount

admin.site.register(BankAccount)

# To create superuser
# python manage.py createsuperuser

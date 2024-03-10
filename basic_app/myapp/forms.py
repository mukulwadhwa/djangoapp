from django import forms
from .models import BankAccount

'''
In your forms.py file within your Django app, 
define a form to capture the necessary data for creating new bank accounts.
'''

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['first_name', 'last_name', 'account_number', 'email', 'balance']

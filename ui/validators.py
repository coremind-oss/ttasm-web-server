import re

from django.contrib.auth.models import User

# Since we are doing it the hard way, we have to write our own validators...
def is_valid_form(form):
    username_len = len(form['username'])
    first_name_len = len(form['first_name'])
    last_name_len = len(form['last_name'])
    password_len = len(form['password1'])
    email_len = len(form['email'])

    def check_lengths():
        if username_len < 1 or username_len > 150:
            return False
        elif first_name_len > 30:
            return False
        elif last_name_len > 30:
            return False
        elif password_len < 8 or password_len > 50:
            return False
        elif email_len < 6 or email_len > 254:
            return False
        return True

    def check_email():
        if re.match(r'[^@]+@[^@]+\.[^@]+', form['email']):
            return True
        return False

    return (check_lengths() and check_email())

# from django.db import models
# from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator,validate_slug,validate_email# Create your models here.
# from django.utils.translation import gettext_lazy as _
#
# def validate_even(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#         )
# class reg(models.Model):
#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
#
#     Name=models.CharField(max_length=30)
#     UserName=models.CharField(max_length=30,unique=True,validators=[alphanumeric])
#     Password=models.CharField(max_length=30,validators=[alphanumeric])
#     Mail=models.EmailField(unique=True)
#     even_field = models.IntegerField(validators=[validate_even])
#     slug_field=models.CharField(max_length=20,validators=[validate_slug])
#     EMail=models.CharField(max_length=20,validators=[validate_email])


from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
import re, bcrypt


def check_uname(value):
    if not re.match('^[.a-zA-Z0-9_]+$', value):
        raise ValidationError('Invalid Username')

def check_passwd(value):
    if len(value) < 8 and not re.search(r'[A-Z]', value) and not re.search(r'[a-z]', value) and not re.search(r'[0-9]', value):
        raise ValidationError('Invalid Password')

# def login(uname, passwd):
#     there = User.objects.filter(user_name=uname).values()
#     if there:
#         if bcrypt.hashpw((passwd).encode(), there[0]['password'].encode()) != there[0]['password'].encode():
#             return  "wrong"
#         else:
#             return there
#
#     else:
#         return "wrong"

class User(models.Model):
      full_name = models.CharField(max_length=45)
      user_name = models.CharField(max_length=45, validators=[check_uname])
      email = models.EmailField(max_length=100)
      password = models.CharField(max_length=100, validators=[check_passwd])
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      paid = models.BooleanField(default=False)
      postal_code = models.CharField(max_length=20)
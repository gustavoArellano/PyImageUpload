from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from datetime import datetime
from time import strftime
from django import forms
from django.conf import settings




EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def RegValidation(self, postData):
        errors = {}

        if len(postData['name']) < 1:
            errors['name'] = "FIRST NAME cannot be BLANK!"
        elif len(postData['name']) < 2:
            errors['name'] = "FIRST NAME must contain at least 2 letters MINIMUM!"
        elif not postData['name'].isalpha():
            errors['name'] = "NAME must contain letter's ONLY!"

        if User.objects.filter(email = postData['email']):
            errors['emailExists'] = "An account has already been created with this EMAIL!"
        if EMAIL_REGEX.match(postData['email']) == None:
            errors['emailFormat'] = "Invalid EMAIL FORMAT!"
        elif len(postData['email']) < 1:
            errors['email'] = "EMAIL cannot be BLANK!"

        if len(postData['password']) < 1:
            errors['password'] = "PASSWORD cannot be BLANK!"
        elif len(postData['password']) < 6:
            errors['passwordLength'] = "PASSWORD must be at least 6 characters MINIMUM!"

        if postData['password'] != postData['confirmPassword']:
            errors['confirmPassword'] = "PASSWORDS do not MATCH!"

        return errors

    def LoginValidation(self, postData):
        user = User.objects.filter(email = postData['loginEmail'])
        errors = {}
        if not user:
            errors['email'] = "Invalid EMAIL or PASSWORD!"

        if user and not bcrypt.checkpw(postData['loginPassword'].encode('utf8'), user[0].password.encode('utf8')):
            errors['password'] = "Invalid EMAIL or PASSWORD!"

        return errors

class User(models.Model): 
    image = models.ImageField(upload_to = 'Users/gustavo/Documents/Coding Random Stuff/PyTestApp/main/apps/MainApp/media', blank=True)
    name = models.CharField(max_length = 20) 
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255, default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

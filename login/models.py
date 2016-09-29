from django.db import models
# from django.contrib.auth.models import User as AuthUser
# Create your models here.
class User(models.Model):
    # user = models.OneToOneField(AuthUser)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__ (self):
        return self.email

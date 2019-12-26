from django.db import models

class Myuser(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)


    def __str__(self):
        return self.lastName
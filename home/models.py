from django.db import models
from django.utils.regex_helper import normalize

class Contact(models.Model):
    name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='teacher', default="default.png")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=55)

    TITLE = (
        ('english','English Teacher'),
        ('scratch','Scratch Teacher'),
        ('science','Science Teacher'),
        ('sport','Sport Teacher'),
    )

    speciality = models.CharField(max_length=55, choices=TITLE)

    def __str__(self):
        return self.name
# Create your models here.

from django.db import models
from django.core.validators import RegexValidator

class PortfolioItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img_path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img_path = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100, validators=[RegexValidator(
        regex="^[a-zA-Z]*$",
        message= "name must be alpha chracters only",
        code= "invalid name"
    )])
    email = models.CharField(null=True, blank=True, max_length=100)
    message = models.TextField(null = True)
    
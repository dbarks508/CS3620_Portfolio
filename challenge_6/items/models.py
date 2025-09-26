from django.db import models

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
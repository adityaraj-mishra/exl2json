from django.db import models

# Create your models here.
class fileupload(models.Model):
    file = models.FileField()


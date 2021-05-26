from django.db import models

# Create your models here.

class image_classification(models.Model):
    img = models.ImageField(upload_to='media')  

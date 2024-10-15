from django.db import models

class Producto(models.Model):
    producto    = models.CharField(max_length=20)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    
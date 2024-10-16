from django.db import models

class Productos(models.Model):
    producto    = models.CharField(max_length=20)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} {self.producto} {self.precio} {self.stock}'
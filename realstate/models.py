from django.db import models

# Create your models here.
class contact_u(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
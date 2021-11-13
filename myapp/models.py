from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class CustomUser(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Email :{self.email}"

    def serialize(self):
        return{
            "id": self.id,
            "First name": self.first_name,
            "Last name": self.last_name,
            "Email": self.email,
        }
            
    

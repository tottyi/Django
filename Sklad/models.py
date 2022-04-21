from django.db import models
from django.views.generic import ListView

# Create your models here.

class Produkt(models.Model):
    nazov = models.TextField()
    partnumber = models.CharField(max_length=20)
    cena = models.CharField(max_length=20)

class Registracia(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    ageold = models.IntegerField()

class ContactListView(ListView):
    paginate_by = 2
    model = Produkt
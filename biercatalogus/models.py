from django.db import models
from django.conf import settings


class Bier(models.Model):
    naam = models.CharField(max_length=200)
    omschrijving = models.TextField()
    picture = models.ImageField()
    barcode = models.CharField(max_length=200)
    
    def __str__(self):
        return self.naam

class BierFles(models.Model):
    bier = models.ForeignKey(Bier, on_delete=models.CASCADE)
    vervaldatum = models.DateTimeField('vervaldatum')
    hoeveelheid = models.IntegerField(default=0)
    prijs = models.IntegerField(default=0)

    def __str__(self):
        return f'Fles {self.bier} ({self.id})'

class BierConsumptie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gelegenheid = models.CharField(max_length=200)
    zuipdatum = models.DateTimeField('vervaldatum')
    biertjes = models.ManyToManyField(BierFles)

    def __str__(self):
        return f'{self.user} drinkt op ({self.zuipdatum})'
    


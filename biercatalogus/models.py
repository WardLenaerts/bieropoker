from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

BEERCOLOR_CHOICES = [
    ('BLOND', 'BLOND'),
    ('BRUIN', 'BRUIN'),
    ('AMBER', 'AMBER'),
]

class Bier(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    beercolor = models.CharField(
        max_length=6,
        choices=BEERCOLOR_CHOICES,
        default="BLOND",)
    content_cl = models.PositiveIntegerField(default=33)
    percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('biercatalogus:product_detail', args=[self.id])
   
    def quantity_subtract(self):
        self.quantity = self.quantity-1
        if self.quantity == 0:
            self.available = False
        return self.quantity

# class Bier(models.Model):
#     naam = models.CharField(max_length=200)
#     omschrijving = models.TextField()
#     picture = models.ImageField()
#     barcode = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.naam

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
    


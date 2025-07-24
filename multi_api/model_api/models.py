from django.db import models

class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    FLAVOUR_CHOICES = [
        ('spicy', 'Spicy'),
        ('non-spicy', 'Non-Spicy'),
    ]
    flavour = models.CharField(max_length=20, choices=FLAVOUR_CHOICES)

    class Meta:
        unique_together = ('name', 'flavour')  # optional, prevents duplicates

    def __str__(self):
        return self.name

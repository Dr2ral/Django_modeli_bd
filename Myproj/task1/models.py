from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=1, max_digits=5)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=1, max_digits=5, blank=False)
    size = models.DecimalField(decimal_places=1, max_digits=4, blank=False)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title

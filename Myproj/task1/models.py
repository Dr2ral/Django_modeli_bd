from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(('Balance'), decimal_places=1, max_digits=4, blank=False, null=True)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(('Cost'), decimal_places=1, max_digits=4, blank=False, null=True)
    size = models.DecimalField(('Size'), decimal_places=1, max_digits=4, blank=False, null=True)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, through='Game_Buyer')


class Game_Buyer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='buyer')

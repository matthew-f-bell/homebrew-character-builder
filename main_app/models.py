from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
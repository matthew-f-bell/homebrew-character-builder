from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
CLASSES_OF_CHARACTERS = {
    ("Rogue", "rogue"),
    ("Bard", "bard"),
    ("Barbarian", "barbarian"),
    ("Cleric", "cleric"),
    ("Druid", "druid"),
    ("Fighter", "fighter"),
    ("Monk", "monk"),
    ("Paladin", "paladin"),
    ("Ranger", "ranger"),
    ("Sorcerer", "sorcerer"),
    ("Warlock", "warlock"),
    ("Wizard", "wizard")
}

class Character_Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    character_class = models.ManyToManyField(Character_Class)
    desc = models.CharField(max_length=2500)

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    race = models.CharField(max_length=50)
    character_class = models.ManyToManyField(Character_Class)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    image = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spells = models.ManyToManyField(Spell)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



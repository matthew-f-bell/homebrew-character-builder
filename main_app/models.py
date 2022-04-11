from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
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

    class Meta:
        ordering = ['name']

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

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
    image = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spells = models.ManyToManyField(Spell, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
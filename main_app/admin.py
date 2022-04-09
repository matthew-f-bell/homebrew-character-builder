from django.contrib import admin
from .models import Character, User, Spell

# Register your models here.

admin.site.register(Character)
admin.site.register(User)
admin.site.register(Spell)
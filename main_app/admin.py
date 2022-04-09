from django.contrib import admin
from .models import Character, User, Spell, Character_Class

# Register your models here.

admin.site.register(Character)
admin.site.register(User)
admin.site.register(Spell)
admin.site.register(Character_Class)
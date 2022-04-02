from email import charset
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

class Home(TemplateView):
        template_name = 'home.html'

class Character:
        def __init__(self, name, age, race, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma, image):
                self.name = name
                self.age = age
                self.race = race
                self.character_class = character_class
                self.strength = strength
                self.dexterity = dexterity
                self.constitution = constitution
                self.intelligence = intelligence
                self.wisdom = wisdom
                self.charisma = charisma
                self.image = image

characters = [
        Character('Eldril', 500, 'Elf', 'Rogue', 18, 16, 12, 9, 12, 10, 'https://blackcitadelrpg.com/wp-content/uploads/2021/12/Timberwatch-Elf-.jpg')
]

class Character_List(TemplateView):
        template_name = 'character_list.html'
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["characters"] = characters
                return context 
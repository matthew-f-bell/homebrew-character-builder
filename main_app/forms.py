from audioop import ratecv
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Character, Character_Class, User, Spell


# Custom Sign-up Form
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

# Custom Character Creation Form
class CharacterCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    age = forms.IntegerField()
    race = forms.CharField(max_length=50)
    character_class = forms.ModelMultipleChoiceField(queryset=Character_Class.objects.all(), widget=forms.CheckboxSelectMultiple)
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    constitution = forms.IntegerField()
    intelligence = forms.IntegerField()
    wisdom = forms.IntegerField()
    charisma = forms.IntegerField()
    image = forms.CharField(max_length=250)
    spells = forms.ModelMultipleChoiceField(queryset=Spell.objects.all(), widget=forms.CheckboxSelectMultiple)

    
    class Meta:
        model = Character
        fields = ['name', 'age', 'race', 'character_class', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'image', 'spells']

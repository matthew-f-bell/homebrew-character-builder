from email import charset
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Character, Spell

# Create your views here.

class Home(TemplateView):
        template_name = 'home.html'

class Character_List(TemplateView):
        template_name = 'character_list.html'
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["characters"] = Character.objects.all()
                return context 

class Character_Create(CreateView):
        model = Character
        fields = '__all__'
        template_name = 'character_create.html'

        def form_valid(self, form):
                self.object = form.save(commit=False)
                self.object.user = self.request.user
                self.object.save()
                return HttpResponseRedirect('/characters')

class Character_Detail(DetailView):
        model = Character
        template_name = 'character_detail.html'

class Character_Update(UpdateView):
        model = Character
        fields = '__all__'
        template_name = 'character_update.html'
        success_url = '/characters/'

class Character_Delete(DeleteView):
        model = Character
        template_name = 'character_delete_confirmation.html'
        success_url = '/characters/'

class Spell_List(TemplateView):
        template_name = 'spell_list.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["spells"] = Spell.objects.all()
            return context

class Spell_Detail(DetailView):
        model = Spell
        template_name = 'spell_detail.html'
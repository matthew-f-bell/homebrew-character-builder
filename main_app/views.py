from django.urls import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, FormView
from django.http import HttpResponseRedirect
from .models import Character, Character_Class, Spell, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegistrationForm, CharacterCreationForm


# Create your views here.

class Home(TemplateView):
        template_name = 'home.html'

class Character_List(TemplateView):
        template_name = 'character_list.html'
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                name = self.request.GET.get("name")
                if name != None:
                        context["characters"] = Character.objects.filter(name__icontains=name)
                else:
                        context["characters"] = Character.objects.all()
                return context

@method_decorator(login_required, name='dispatch')
class Character_Create(FormView):
        model = Character
        form_class = CharacterCreationForm
        template_name = 'character_create.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['spells'] = Spell.objects.all()
            context['char_classes'] = Character_Class.objects.all()
            return context

        def form_valid(self, form):
                self.object = form.save(commit=False)
                self.object.user = self.request.user
                self.object.save()
                return HttpResponseRedirect('/characters')

@method_decorator(login_required, name='dispatch')
class Character_Detail(DetailView):
        model = Character
        template_name = 'character_detail.html'

@method_decorator(login_required, name='dispatch')
class Character_Update(UpdateView):
        model = Character
        form_class = CharacterCreationForm
        template_name = 'character_update.html'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['spells'] = Spell.objects.all()
            context['char_classes'] = Character_Class.objects.all()
            return context

        success_url = '/characters/'

@method_decorator(login_required, name='dispatch')
class Character_Delete(DeleteView):
        model = Character
        template_name = 'character_delete_confirmation.html'
        success_url = '/characters/'

def spell_list(request):
        spells = Spell.objects.all()
        return render(request, 'spell_list.html', {'spells': spells})

def spell_detail(request, spell_id):
        spell = Spell.objects.get(id=spell_id)
        return render(request, 'spell_detail.html', {'spell': spell})

def login_view(request):
        if request.method == 'POST':
                form = AuthenticationForm(request, request.POST)
                if form.is_valid():
                        u = form.cleaned_data['username']
                        p = form.cleaned_data['password']
                        user = authenticate(username = u, password = p)
                        if user is not None:
                                if user.is_active:
                                        login(request, user)
                                        return HttpResponseRedirect('/')
                                else:
                                        return render(request, 'login.html', {'form': form})
                        else: 
                                return render(request, 'login.html', {'form': form})
                else:
                        return render(request, 'signup.html', {'form': form})
        else:
                form = AuthenticationForm()
                return render(request, 'login.html', {'form': form})

def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/characters')

def signup_view(request):
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        user.refresh_from_db()
                        user.first_name = form.cleaned_data.get('first_name')
                        user.last_name = form.cleaned_data.get('last_name')
                        user.email = form.cleaned_data.get('email')
                        user.save()
                        login(request, user)
                        print('HEY ', user.first_name)
                        return HttpResponseRedirect('/login')
                else:
                        return render(request, 'signup.html', {'form': form})
        else:
                form = RegistrationForm()
                return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, user_id):
        user = User.objects.get(id=user_id)
        characters = Character.objects.filter(user=user)
        return render(request, 'profile.html', {'id': id, 'characters': characters})

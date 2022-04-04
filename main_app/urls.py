from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('characters/', views.Character_List.as_view(), name="character-list"),
    path('character/new/', views.Character_Create.as_view(), name="character-create")
]
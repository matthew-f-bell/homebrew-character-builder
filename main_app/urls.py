from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('characters/', views.Character_List.as_view(), name="character-list"),
    path('characters/new/', views.Character_Create.as_view(), name="character-create"),
    path('characters/<int:pk>/', views.Character_Detail.as_view(), name="character-detail"),
]
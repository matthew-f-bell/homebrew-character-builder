from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('characters/', views.Character_List.as_view(), name="character-list"),
    path('characters/new/', views.Character_Create.as_view(), name="character-create"),
    path('characters/<int:pk>/', views.Character_Detail.as_view(), name="character-detail"),
    path('characters/<int:pk>/update', views.Character_Update.as_view(), name="character-update"),
    path('characters/<int:pk>/delete', views.Character_Delete.as_view(), name="character-delete"),
    path('spells/', views.Spell_List.as_view(), name="spell-list"),
    path('spells/<int:spells_id>', views.Spell_Detail.as_view(), name="spell-detail"),
]
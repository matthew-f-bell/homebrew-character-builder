from django.urls import path
from . import views

urlpatterns = [
    path('', views.Character_List.as_view(), name='home'),
    path('characters/', views.Character_List.as_view(), name="character-list"),
    path('characters/new/', views.Character_Create.as_view(), name="character-create"),
    path('characters/<int:pk>/', views.Character_Detail.as_view(), name="character-detail"),
    path('characters/<int:pk>/update', views.Character_Update.as_view(), name="character-update"),
    path('characters/<int:pk>/delete', views.Character_Delete.as_view(), name="character-delete"),
    path('spells/', views.spell_list, name="spell-list"),
    path('spells/<int:spell_id>', views.spell_detail, name="spell-detail"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),
    path('user/<int:user_id>/', views.profile, name="profile")
]
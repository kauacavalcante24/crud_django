from django.urls import path
from .views import get_users, get_by_nick, user_manager


urlpatterns = [
    path('', get_users, name='get_all_users'),
    path('user/<str:nick>', get_by_nick, name='get_by_nick'),
    path('data/', user_manager, name='user_manager')
]

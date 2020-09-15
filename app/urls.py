from django.urls import path
from django.conf.urls import include
from app import views
from .views import login, home, logout_user

app_name = 'app'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home')
]
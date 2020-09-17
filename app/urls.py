from django.urls import path, include 
from . import views

app_name = 'app'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('symptomEntries', views.symptomEntries_list, name='symptomEntries')
]
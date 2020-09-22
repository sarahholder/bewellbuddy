from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'app'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('entries', views.entries_list, name='entries'),
    path('entryform', views.entry_form, name='entryform'),
    path('medicines', views.medicines_list, name='medicines'),
    path('medicine_detail/<int:medicine_id>', views.medicine_detail, name='medicine_detail'),
    path('medicine_form', views.medicine_form, name="medicine_form"),
    path('archived_medicine', views.archived_medicines_list, name="archived_medicine"),
    path('archived_medicine/<int:medicine_id>', views.archived_medicines_list, name="archived_medicine")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
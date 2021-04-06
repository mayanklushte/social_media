from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_register', views.admin_register, name='admin_register'),
    path('user_login/', views.user_login, name='user_login')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
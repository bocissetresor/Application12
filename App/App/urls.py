from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from Application12 import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('register/', app_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='Application12/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Application12/logout.html'), name='logout'),
]
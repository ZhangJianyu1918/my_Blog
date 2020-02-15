from . import views
from django.contrib.auth import login
from django.conf.urls import url

urlpatterns = [
    url('login/', views.login_view,name='login'),
    url('logout/',views.logout_view, name='logout'),
    url('register/',views.register, name='register'),
]

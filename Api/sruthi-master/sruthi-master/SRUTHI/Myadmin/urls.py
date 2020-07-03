from django.urls import path

from . import views

urlpatterns = [
    path('',views.Myadmin, name='Myadmin'),
    path('admin-login',views.admin_login, name='admin_login'),
    path('hi',views.hi,name='hi'),
    path('hi1',views.hi1,name='hi1'),
]
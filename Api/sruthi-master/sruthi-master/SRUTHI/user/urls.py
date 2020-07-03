from django.urls import path

from . import views

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('user_login/api_call',views.api_call,name='api'),
    path('user_registration/registration',views.registration,name='registration'),
    path('user_login/<int:Rollno>/',views.profile,name='profile'),
   
    path('user_login/<int:Rollno>/EventReg',views.EventsReg,name='EventsReg'),
   
    path('user_login/Events',views.Events,name='Events'),
  
    path('user_login/eventreg/<int:user_id>/',views.Eventregistration,name='Eventregistration'),
  
    path('user_login/eventreg/<int:user_id>/reg',views.reg,name='reg'),
    
    path('user_login/fav/<int:user_id>/',views.fav,name="fav"),
    ]
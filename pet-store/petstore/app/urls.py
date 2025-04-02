from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('petdetails/<int:petid>/', views.petdetails, name='petdetails')     
         
]

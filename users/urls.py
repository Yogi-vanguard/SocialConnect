from django.urls import path
from . import views

urlpatterns=[
    path('',views.profiles,name="profiles"),
    path('profile/<str:pk>/',views.userprofile,name="user-profile"),
    path('login/',views.LoginUser,name="login"),
    path('logout/',views.LogoutUser,name='logout'),
    path('register/',views.RegisterUser,name='register'),
    path('account/',views.userAccount,name='account'),
]
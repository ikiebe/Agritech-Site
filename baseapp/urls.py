from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    
    path('logout/', views.logoutUser, name="logout"),
    path('careers/', views.careers, name="careers"),
    path('desc/<str:pk>/', views.careerDesc, name="careerDesc"),
    path('login/', views.loggin, name="login_register"),
    path('signup/', views.sign_up, name="sign_up"),
    path('apply/', views.applicationPage, name="apply")
]

handler404 = 'baseapp.views.error404'
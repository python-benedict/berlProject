from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('detaileduser/', views.detaileduser, name='detaileduser'),
    path('chooseroom/', views.chooseroom, name='chooseroom'),
]

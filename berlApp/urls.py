from django.urls import path
from . import views
urlpatterns = [
    path('', views.detaileduser, name='detaileduser'),
    path('chooseroom/', views.chooseroom, name='chooseroom'),
]

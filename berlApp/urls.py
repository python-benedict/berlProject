from django import path
from . import views
urlpatterns = [
    path('', views.detailedUser, name='detailedUser'),
]
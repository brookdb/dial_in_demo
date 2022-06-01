from django.urls import path
from .import views

app_name = 'apps.brew'

urlpatterns = [
    path('', views.brew_landing, name="brew_landing"), #landing page
    path('add', views.brew_add, name="add"),
    path('<slug:slug>', views.brew_details, name="brew_details"),
]

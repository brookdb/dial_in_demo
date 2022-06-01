from django.urls import path
from .import views

app_name = 'apps.roast'

urlpatterns = [
    path('', views.roast_landing, name="roast_landing"), #landing page
    path('add', views.roast_add, name="add"),
    #path('search', views.SearchResultsList.as_view(), name="roast_search"),
    path('<slug:slug>', views.roast_detail, name="detail"),

]

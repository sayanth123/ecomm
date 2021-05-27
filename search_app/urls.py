from django.urls import path,include
from . import views
app_name='search_app'
urlpatterns = [
    path('s/', views.Search_Results,name='Search_Results'),


]
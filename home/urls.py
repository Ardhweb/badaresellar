from django.urls import path

from home.views import home_index

from home import views



urlpatterns = [
    path('', views.home_index, name="index"),

    
]

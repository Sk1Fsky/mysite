from django.urls import path
from app import views
urlpatterns = [
     path(r'', views.HomePage.as_view())
]

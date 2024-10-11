from django.urls import path
from . import views

app_name = "about"
urlpatterns = [
    path("mateo_vergara", views.mateo_vergara, name = "mateo_vergara"),
]

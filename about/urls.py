from django.urls import path
from . import views

app_name = "about"
urlpatterns = [
    path("mateo_vergara", views.mateo_vergara, name = "mateo_vergara"),
    path("terms_and_conditions", views.terms_and_conditions, name = "terms_and_conditions"),
]

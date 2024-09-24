from django.urls import path
from . import views

app_name = "calculations"
urlpatterns = [
    path("cable_calculation", views.cable_calculation, name = "cable_calculation"),
    path("cable_result", views.cable_result, name = "cable_result"),
    path("drop_voltage", views.drop_voltage, name = "drop_voltage"),
    path("protective_device", views.protective_device, name = "protective_device"),
    path("grounding_cable", views.grounding_cable, name = "grounding_cable"),
    path("conduits_calculation", views.conduit_calculation, name = "conduit_calculation"),
    path("conduits_result", views.conduit_result, name = "conduit_result"),
    path("work_clearances_calculation", views.work_clearances_calculation, name = "work_clearances_calculation"),
    path("work_clearances_result", views.work_clearances_result, name = "work_clearances_result"),
    path("safety_clearances_calculation", views.safety_clearances_calculation, name = "safety_clearances_calculation"),
    path("safety_clearances_result", views.safety_clearances_result, name = "safety_clearances_result"),
    path("arcflash_calculation", views.arcflash_calculation, name = "arcflash_calculation"),
    path("arcflash_result", views.arcflash_result, name = "arcflash_result"),
]

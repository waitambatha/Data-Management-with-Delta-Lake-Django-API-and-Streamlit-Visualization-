from django.urls import path
from .views import employee_data

urlpatterns = [
    path("employee-data/", employee_data, name="employee_data"),
]
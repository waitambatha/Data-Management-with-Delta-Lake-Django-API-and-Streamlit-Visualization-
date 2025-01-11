from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # Include URLs from the employee app
    path("api/", include("employee.urls")),
]
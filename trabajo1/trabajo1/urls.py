
from django.contrib import admin
from django.urls import path
from trabajo1.views import familia



urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia/",familia),
]


from django.contrib import admin
from django.urls import path, include
from demands import urls as demands_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demand/', include(demands_urls))
]

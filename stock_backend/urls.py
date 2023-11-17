from django.contrib import admin
from django.urls import include, path

url_patterns = [
    path('admin/', admin.site.urls),
    path('', include('stock_backend.urls'))
]
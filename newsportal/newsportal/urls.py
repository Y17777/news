from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path("accounts/", include("accounts.urls")),
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    ]

# http://127.0.0.1:8000/admin
# http://127.0.0.1:8000/pages
#  http://127.0.0.1:8000/news

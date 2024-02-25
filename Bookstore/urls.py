from django.contrib import admin
from django.urls import path, include
from Bookstore_api import urls as api_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
    path("accounts/",include(accounts_urls))
]


from django.contrib import admin
from django.urls import path, include

# static files
from django.conf import settings
from django.conf.urls.static import static

# to wrong sites
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('safe.urls')),
    path('', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def page_not_found(request, exception=None):
    return HttpResponse("Page not found", status=404)


def bad_request(request, exception=None):
    return HttpResponse("Bad request", status=400)


def custom_error(request, exception=None):
    return HttpResponse("Custom error", status=500)


handler403 = response_error_handler
handler404 = page_not_found
handler400 = bad_request
handler500 = custom_error

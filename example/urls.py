import django
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url, include
from django.contrib import admin
from rango import views

urlpatterns = [
    url(r'^rango/', include('rango.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
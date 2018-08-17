from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
]

from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.urls import include

from movies.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/now-playing', get_now_playing),
    url(r'^watchlist/', include('watchlist.urls')),
]

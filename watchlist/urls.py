from django.urls import include, path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from rest_framework import routers

from .views import WatchlistView


app_name = "watchlist"


urlpatterns = [
    path('<int:pk>/', WatchlistView.as_view()),
    path('', WatchlistView.as_view()),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


from django.conf import settings
import requests


class MoviesService(object):
    @staticmethod



    def fetch_now_playing():
        url = settings.TMDB_BASE_URL + settings.TMDB_VERSION_3 +  settings.TMDB_MOVIE + settings.TMDB_NOW_PLAYING
        r = requests.get( url + '?api_key=' + settings.TMDB_API_KEY + '&page=1')
        json = r.json()

        for res in json["results"]:
            res["poster_path"] = settings.TMDB_IMAGE_URL + res["poster_path"]

        return json

        
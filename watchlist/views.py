from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import WatchlistSerializer
from .models import WatchList


class WatchlistView(APIView):
    def get(self, request, pk=None):
        if pk:
            watchlist = get_object_or_404(WatchList.objects.all(), pk=pk)
            serializer = WatchlistSerializer(watchlist)
            return Response({"watchlist": serializer.data})
        watchlists = WatchList.objects.all()
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response({"watchlist": serializer.data})

    def post(self, request):
        watchlist = request.data.get('watchlist')

        serializer = WatchlistSerializer(data=watchlist)
        if serializer.is_valid(raise_exception=True):
            watchlist_saved = serializer.save()
        return Response({"success": "watchlist '{}' created successfully".format(watchlist_saved.title)})

    def put(self, request, pk, format=None):
        pk = self.kwargs.get('pk')
        print("PK"+str(pk))
        saved_watchlist = get_object_or_404(WatchList.objects.all(), pk=pk)
        data = request.data.get('watchlist')
        serializer = WatchlistSerializer(instance=saved_watchlist, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            watchlist_saved = serializer.save()
        return Response({"success": "watchlist '{}' updated successfully".format(watchlist_saved.title)})


    def delete(self, request, pk):
        # Get object with this pk
        watchlist = get_object_or_404(watchlist.objects.all(), pk=pk)
        watchlist.delete()
        return Response({"message": "watchlist with id `{}` has been deleted.".format(pk)},status=204)

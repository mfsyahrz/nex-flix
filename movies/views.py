# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import MoviesService

@api_view(['GET', 'POST', ])
def get_now_playing(request):
    if request.method == "GET":
      result = MoviesService.fetch_now_playing()
      return Response(result, status=status.HTTP_200_OK)
    else :
      return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)      



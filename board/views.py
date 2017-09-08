# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from .models import Sprint
from .serializers import SprintSerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
     filtering and pagination."""

     authentication_classes = (
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
     )
     permission_classes = (
         permissions.IsAuthenticated,
     )
     paginate_by = 25
     paginate_by_param = 'page_size'
     max_paginate_by = 100

class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """"API Endpoint for listing and creating sprints."""
    query_set = Sprint.objects.order_by('end_date')
    serializer_class = SprintSerializer

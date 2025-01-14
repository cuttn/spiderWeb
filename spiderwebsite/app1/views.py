from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from itertools import chain
from .models import client, influencer
import django_filters
from rest_framework import permissions, viewsets, filters
from .serializers import clientSerializer, influencerSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def globalSearch(request,query):
    if len(query) < 2:
        return Response([])
    clients = client.objects.filter(Q(name__icontains=query))
    influencers = influencer.objects.filter(Q(name__icontains=query))
    results = list(chain(clients, influencers))
    return Response([{
        'name': result.name,
        'type': 'client' if isinstance(result, client) else 'influencer'
    } for result in results])
    
class clientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = client.objects.all().order_by('name')
    serializer_class = clientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name",]

class influencerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = influencer.objects.all().order_by('name')
    serializer_class = influencerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name",]
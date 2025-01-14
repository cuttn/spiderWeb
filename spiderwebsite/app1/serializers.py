from .models import influencer, client
from rest_framework import serializers


class influencerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = influencer
        fields = ['name', 'trust', 'links', 'audience_tags', 'niche_tags']


class clientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = client
        fields = ['influencers', 'name']
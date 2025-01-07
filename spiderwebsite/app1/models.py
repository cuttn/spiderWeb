from django.db import models
from django.core.cache import cache
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
import asyncio
import aiohttp
from urllib.parse import urlparse
import re

class client(models.Model):
    influencers = models.ManyToManyField('influencer', related_name='client_set')

class campaign(models.Model):
    client = models.ForeignKey('client', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    influencers = models.ManyToManyField('influencer', through='CampaignInfluencer', related_name='campaigns')

class CampaignInfluencer(models.Model):
    campaign = models.ForeignKey(campaign, on_delete=models.CASCADE)
    influencer = models.ForeignKey('influencer', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='active'
    )

# Add these classes before your influencer model
class AudienceTag(TaggedItemBase):
    pass

class NicheTag(TaggedItemBase):
    pass

# Create your models here.
class influencer(models.Model):
    adjacent_influencers = models.ManyToManyField('self', symmetrical=False, blank=True)
    audience = TaggableManager(through=AudienceTag, related_name="audience")
    niches = TaggableManager(through=NicheTag, related_name="niches")
    trust = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)
    links = models.TextField()    
    def get_popularity(self):
        cache_key = f'influencer_popularity_{self.id}'
        popularity = cache.get(cache_key)
        
        if popularity is None:
            # Run async code in sync context
            popularity = asyncio.run(self._gather_all_stats())
            cache.set(cache_key, popularity, timeout=3600)
            
        return popularity
    
    async def _gather_all_stats(self):
        """Gather stats from all platforms asynchronously"""
        links = self.get_links()
        total_score = 0
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for link in links:
                domain = urlparse(link).netloc
                
                if 'youtube.com' in domain:
                    tasks.append(self._get_youtube_stats(session, link))
                # Add other platforms here
            
            # Wait for all tasks to complete
            scores = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Sum up all valid scores
            total_score = sum(score for score in scores if isinstance(score, int))
            
        return total_score
    
    async def _get_youtube_stats(self, session, link):
        """Get YouTube stats asynchronously"""
        API_KEY = 'your_api_key_here'
        channel_id = self._extract_youtube_id(link)
        
        if not channel_id:
            return 0
            
        url = 'https://www.googleapis.com/youtube/v3/channels'
        params = {
            'part': 'statistics',
            'id': channel_id,
            'key': API_KEY
        }
        
        try:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['items']:
                        stats = data['items'][0]['statistics']
                        return int(stats['subscriberCount'])
        except Exception as e:
            print(f"Error getting YouTube stats: {e}")
        
        return 0
    
    def _extract_youtube_id(self, url):
        if '/channel/' in url:
            return url.split('/channel/')[1].split('/')[0]
        elif '/c/' in url or '/user/' in url:
            username = url.split('/')[-1]
            return self._get_channel_id_from_username(username)
        return None

    def get_links(self):
        # Split the string into a list of links
        return self.links.split(',')

    def set_links(self, links):
        # Join a list of links into a comma-separated string
        self.links = ','.join(links)
            
    def _get_channel_id_from_username(self, username):
        # Implementation of _get_channel_id_from_username method
        pass

    

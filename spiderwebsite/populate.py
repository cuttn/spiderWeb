import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spiderwebsite.settings')
django.setup()

# After django.setup(), we can import Django-related modules
from app1.models import client, campaign, influencer, CampaignInfluencer
from django.utils import timezone

# Create a test client
test_client = client.objects.create(
    name="TestClient_asdf"
)
    
# Create a test influencer with string tags
test_influencer = influencer.objects.create(
    name="TestInfluencer_asdf",
    trust=84,
    links="https://youtube.com/test_asdf,https://instagram.com/test_asdf",
    audience_tags="teens_asdf,students_asdf",
    niche_tags="education_asdf,lifestyle_asdf"
)

# Create a test campaign
test_campaign = campaign.objects.create(
    client=test_client,
    start_date=timezone.now()
)

# Link the influencer to the campaign
CampaignInfluencer.objects.create(
    campaign=test_campaign,
    influencer=test_influencer
)
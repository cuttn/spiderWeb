from app1.models import client, campaign, influencer, CampaignInfluencer
from django.utils import timezone

# Create a test client
test_client = client.objects.create(
    name="TestClient_6"
)
    
# Create a test influencer with string tags
test_influencer = influencer.objects.create(
    name="TestInfluencer_6",
    trust=85,
    links="https://youtube.com/test_6,https://instagram.com/test_6",
    audience_tags="teens_6,students_6",
    niche_tags="education_6,lifestyle_6"
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
# Generated by Django 5.1.4 on 2025-01-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influencer',
            name='audience',
        ),
        migrations.RemoveField(
            model_name='nichetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='influencer',
            name='niches',
        ),
        migrations.RemoveField(
            model_name='influencer',
            name='adjacent_influencers',
        ),
        migrations.AddField(
            model_name='influencer',
            name='audience_tags',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='influencer',
            name='niche_tags',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AudienceTag',
        ),
        migrations.DeleteModel(
            name='NicheTag',
        ),
    ]

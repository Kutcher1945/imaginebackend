# Generated by Django 4.0.3 on 2024-06-25 04:19

from django.db import migrations

def create_initial_analytics(apps, schema_editor):
    Analytics = apps.get_model('analytics', 'Analytics')
    Analytics.objects.create(
        page_views=0,
        unique_users=0,
        active_sessions=0,
        bounce_rate=0.0,
        most_popular_section='None'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_analytics),
    ]

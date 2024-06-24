from django.contrib import admin
from .models import Analytics

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('page_views', 'unique_users', 'active_sessions', 'bounce_rate', 'most_popular_section')

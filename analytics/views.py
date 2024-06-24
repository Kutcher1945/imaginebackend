from django.http import JsonResponse
from .models import Analytics

def get_analytics_data(request):
    analytics = Analytics.objects.first()  # Assuming you have one analytics object
    data = {
        'pageViews': analytics.page_views,
        'uniqueUsers': analytics.unique_users,
        'activeSessions': analytics.active_sessions,
        'bounceRate': analytics.bounce_rate,
        'mostPopularSection': analytics.most_popular_section,
    }
    return JsonResponse(data)

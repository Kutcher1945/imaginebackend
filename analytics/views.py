from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Analytics

@csrf_exempt
def update_analytics_data(request):
    if request.method == 'POST':
        try:
            data = request.json()
            analytics, created = Analytics.objects.get_or_create(id=1)
            analytics.page_views += data.get('pageViews', 0)
            analytics.unique_users += data.get('uniqueUsers', 0)
            analytics.active_sessions += data.get('activeSessions', 0)
            analytics.bounce_rate = data.get('bounceRate', analytics.bounce_rate)
            analytics.most_popular_section = data.get('mostPopularSection', analytics.most_popular_section)
            analytics.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def get_analytics_data(request):
    analytics = Analytics.objects.first()
    if analytics is None:
        # Return default values if no Analytics object exists
        data = {
            'pageViews': 0,
            'uniqueUsers': 0,
            'activeSessions': 0,
            'bounceRate': 0.0,
            'mostPopularSection': 'None',
        }
    else:
        data = {
            'pageViews': analytics.page_views,
            'uniqueUsers': analytics.unique_users,
            'activeSessions': analytics.active_sessions,
            'bounceRate': analytics.bounce_rate,
            'mostPopularSection': analytics.most_popular_section,
        }
    return JsonResponse(data)

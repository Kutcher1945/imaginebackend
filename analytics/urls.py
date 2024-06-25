from django.urls import path
from .views import get_analytics_data, update_analytics_data

urlpatterns = [
    path('analytics-data/', get_analytics_data, name='analytics-data'),
    path('update-analytics/', update_analytics_data, name='update-analytics'),
]

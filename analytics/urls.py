from django.urls import path
from .views import get_analytics_data

urlpatterns = [
    path('analytics-data/', get_analytics_data, name='analytics-data'),
]

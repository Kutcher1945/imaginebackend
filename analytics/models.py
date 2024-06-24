from django.db import models

class Analytics(models.Model):
    page_views = models.IntegerField(default=0)
    unique_users = models.IntegerField(default=0)
    active_sessions = models.IntegerField(default=0)
    bounce_rate = models.FloatField(default=0.0)
    most_popular_section = models.CharField(max_length=255, default='Home')

    def __str__(self):
        return f"Analytics({self.page_views}, {self.unique_users}, {self.active_sessions}, {self.bounce_rate}, {self.most_popular_section})"

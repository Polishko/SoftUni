from django.db.models import Count
from django.db import models


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        profiles = (self.prefetch_related("profile_orders").
                    annotate(num_orders=Count("profile_orders")).
                    filter(num_orders__gt=2).order_by("-num_orders"))

        return profiles

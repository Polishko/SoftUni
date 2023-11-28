from django.db.models import Count
from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        return (self.
                prefetch_related("articles").
                annotate(num_articles=Count("articles")).
                order_by("-num_articles", "email")
                )


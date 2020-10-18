from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from django.db.models import Subquery, OuterRef, Count
from django.utils import timezone

from apps.news.models import Post


@periodic_task(run_every=(timezone.timedelta(hours=24)))
def reset_post_upvotes_count_task():
    Post.objects.update(
        amount_of_upvotes=Subquery(Post.objects.filter(id=OuterRef('id')).values(upvotes_count=Count('postvotes'))[:1]))


@periodic_task(run_every=(timezone.timedelta(minutes=2)))
def raise_val_error():
    raise ValueError

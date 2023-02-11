from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from news.models import *

@shared_task
def notify_about_new_post():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(timeCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'weekly_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,

        }
    )

    msg = EmailMultiAlternatives(
        subject='Публикации за неделю',
        body='',
        from_email=None,
        to=subscribers,

    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
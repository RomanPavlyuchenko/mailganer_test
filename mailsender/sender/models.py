from datetime import datetime
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.email


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    html_content = models.TextField()

    def __str__(self):
        return self.subject


class EmailCampaign(models.Model):
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(Subscriber)
    scheduled_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
    celery_task_id = models.CharField(default='', max_length=36)

    def __str__(self):
        return self.template.subject


class EmailSubscriber(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    campaign = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE)
    sent_time = models.DateTimeField(default=datetime.now)
    opened = models.BooleanField(default=False)
    tracking_pixel = models.UUIDField(unique=True, default=None, null=True)

    def __str__(self):
        return self.subscribers.email

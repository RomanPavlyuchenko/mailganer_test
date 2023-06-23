from datetime import datetime
from uuid import uuid4

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import EmailCampaign, EmailSubscriber


@shared_task
def send_email_campaign(campaign_id):
    campaign = EmailCampaign.objects.get(pk=campaign_id)
    campaign.celery_task_id = send_email_campaign.request.id
    campaign.save()
    subscribers = campaign.subscribers.all()
    template = campaign.template
    for subscriber in subscribers:
        subject = template.subject
        html_message = template.html_content.format(
            first_name=subscriber.first_name,
            last_name=subscriber.last_name,
            birthday=subscriber.birthday,
            subject=subject
        )

        tracking_uuid = uuid4()
        html_message += '<img src="{}" width="1" height="1" alt="Pixel">'.format(
            tracking_uuid
        )

        send_mail(
            subject, '', settings.EMAIL_HOST_USER,
            [subscriber.email], html_message=html_message
        )
        sent_mail = EmailSubscriber.objects.create(
            subscriber=subscriber,
            campaign=campaign,
            tracking_pixel=tracking_uuid
        )
        sent_mail.save()

    campaign.sent = True
    campaign.save()


@shared_task
def process_scheduled_emails():
    now = datetime.now()
    emails_to_send = EmailCampaign.objects.filter(
        scheduled_time__lte=now, sent=False, celery_task_id=''
    )

    for email in emails_to_send:
        send_email_campaign.delay(email.id)

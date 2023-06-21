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
    tracking_pixel = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.subject


class EmailCampaign(models.Model):
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(Subscriber)
    scheduled_time = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.template.subject

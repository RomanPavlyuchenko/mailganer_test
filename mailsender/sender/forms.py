from django import forms
from .models import EmailCampaign


class CreateEmailCampaignForm(forms.ModelForm):
    class Meta:
        model = EmailCampaign
        fields = ['template', 'scheduled_time']

        widgets = {
            'scheduled_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker',
                    'data-date-start-date': '0d'
                }
            ),
        }

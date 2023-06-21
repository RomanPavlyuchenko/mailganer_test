from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from .forms import CreateEmailCampaignForm
from .models import EmailCampaign, Subscriber


def home(request):
    return render(request, 'sender/home.html')


class CreateEmailCampaignView(FormView):
    template_name = 'sender/create_email_campaign.html'
    form_class = CreateEmailCampaignForm
    success_url = reverse_lazy('campaign_list')

    def form_valid(self, form):
        campaign = EmailCampaign.objects.create(
            template=form.cleaned_data['template'],
            scheduled_time=form.cleaned_data['scheduled_time']
        )
        campaign.subscribers.set(Subscriber.objects.all())
        campaign.save()
        messages.success(self.request, 'Email campaign created successfully!')
        return super(FormView, self).form_valid(form)


class EmailCampaignListView(ListView):
    model = EmailCampaign
    template_name = 'sender/email_campaign_list.html'
    context_object_name = 'campaigns'


class EmailCampaignDetailView(DetailView):
    model = EmailCampaign
    template_name = 'sender/email_campaign_detail.html'
    context_object_name = 'campaign'

    def get(self, request, *args, **kwargs):
        campaign = EmailCampaign.objects.get(pk=kwargs['pk'])
        return render(request, 'sender/email_campaign_detail.html', {'campaign': campaign})

    def get_context_data(self, **kwargs):
        context = super(EmailCampaignDetailView, self).get_context_data(**kwargs)
        campaign = context['campaign']
        context['send_url'] = reverse('send_campaign', args=[campaign.pk])
        return context


class SendEmailCampaignView(View):
    def post(self, request, pk):
        return redirect('campaign_list')

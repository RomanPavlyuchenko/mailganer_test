from django.conf.urls import url

from .views import (
    CreateEmailCampaignView,
    EmailCampaignListView,
    EmailCampaignDetailView,
    SendEmailCampaignView,
    home
)


urlpatterns = [
    url(r'^create/$', CreateEmailCampaignView.as_view(), name='create_campaign'),
    url(r'^list/$', EmailCampaignListView.as_view(), name='campaign_list'),
    url(r'^detail/(?P<pk>\d+)/$', EmailCampaignDetailView.as_view(), name='campaign_detail'),
    url(r'^send/(?P<pk>\d+)/$', SendEmailCampaignView.as_view(), name='send_campaign'),

    url('', home, name='home')

]

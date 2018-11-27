from django.conf.urls import url
from . import views as events_views

app_name = 'events'


urlpatterns = [
	url(r'^wsoc2018/', events_views.wsoc2018, name='wsoc'),
	url(r'^hackathon/blockhack2019', events_views.blockhack2019, name='blockhack'),
	url(r'^meetup/blockchain_in_business', events_views.blockchain_in_business, name='events'),
	url(r'^meetup/streethack_2019_1', events_views.streethack_2019_1, name='events'),
	url(r'^$', events_views.index, name='events'),

]

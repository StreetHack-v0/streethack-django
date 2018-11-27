from django.conf.urls import url
from . import views as university_views

app_name = 'university'


urlpatterns = [
	url(r'^why/', university_views.why, name='university_why'),
	url(r'^products/', university_views.products, name='university_products'),
	url(r'^features/', university_views.features, name='university_features'),
	url(r'^pricing/', university_views.pricing, name='university_pricing'),
	url(r'^contact_us/', university_views.contact_us, name='university_contact_us'),
	url(r'^get_started/', university_views.get_started, name='university_get_started'),
	url(r'^$', university_views.index, name='university'),
]

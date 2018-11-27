from django.conf.urls import url
from . import views as enterprise_views

app_name = 'enterprise'


urlpatterns = [
	url(r'^why/', enterprise_views.why, name='enterprise_why'),
	url(r'^products/', enterprise_views.products, name='enterprise_products'),
	url(r'^features/', enterprise_views.features, name='enterprise_features'),
	url(r'^pricing/', enterprise_views.pricing, name='enterprise_pricing'),
	url(r'^contact_us/', enterprise_views.contact_us, name='enterprise_contact_us'),
	url(r'^get_started/', enterprise_views.get_started, name='enterprise_get_started'),
	url(r'^$', enterprise_views.index, name='enterprise'),

]

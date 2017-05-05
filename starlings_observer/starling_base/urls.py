from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
  	url(r'^admin/', admin.site.urls),
  	url(r'^profile/$', views.profile, name='profile'),
	url(r'^search/$', views.search, name='search'),
	url(r'^starling_detail/(?P<number>JMZ.+)/', views.starling_detail, name='starling_detail'),
	url(r'^$', views.home, name='home'),
	url(r'^add_death/$', views.add_death, name='add_death'),
	url(r'^add_collection/$', views.add_collection, name='add_collection'),
	url(r'^add_identifiers/$', views.add_identifiers, name='add_identifiers'),
	url(r'^add_complex_traits/$', views.add_complex_traits, name='add_complex_traits'),
	url(r'^add_preparation/$', views.add_preparation, name='add_preparation'),
	url(r'^add_location/$', views.add_location, name='add_location'),
	url(r'^add_skin/$', views.add_skin, name='add_skin'),
	url(r'^add_pre_skin/$', views.add_pre_skin, name='add_pre_skin'),

	
]

	

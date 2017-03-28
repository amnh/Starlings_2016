from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
  	url(r'^admin/', admin.site.urls),
  	url(r'^profile/$', views.profile, name='profile'),
	url(r'^search/$', views.search, name='search'),
	url(r'^add_death/$', views.add_death, name='add_death'),
	url(r'^home/$', views.home, name='home'),
	url(r'^new_york/$', views.state, name='new_york'),

]
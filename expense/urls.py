from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('new', views.new_expense, name = 'new_expense'),
	url(r'^login$', auth_views.login, {'template_name':'expense/login.html'}, name='login'),


]
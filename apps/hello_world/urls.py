from django.urls import path
from apps.hello_world import views

urlpatterns = [
	path('', views.hello_world, name='hello_world')
]

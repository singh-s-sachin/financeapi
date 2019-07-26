from django.urls import path,include
from . import views
from rest_framework import routers

#router.register('accounts',views.accountview)
urlpatterns = [
	path('create/',views.open),
	path('fd',views.fd),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createpay', views.createpay),
    path('confirmpay', views.confirmpay),
]



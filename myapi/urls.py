from django.urls import path
from . import views

urlpatterns = [
    # Payment Transfer API
    path('ReceivingData/', views.ReceivingData, name='ReceivingData'),
    path('ReceivingDataTest/', views.ReceivingDataTest, name='ReceivingDataTest'),
]
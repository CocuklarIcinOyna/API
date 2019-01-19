
from django.urls import path
from cocuklaricin_api import views

urlpatterns = [
    path('machine/<int:pk>', views.MachineView.as_view()), #get only one machine
    path('machines/', views.MachineViewSet.as_view({'get':'list'})), #get all machines
    path('fund/<int:pk>', views.FundView.as_view()), #get or delete fund
    path('create_fund', views.FundView.as_view()), #create new fund, send POST method
    path('campaign/<int:pk>', views.CampaignView.as_view()), #get campaign
    path('campaigns/', views.CampaignViewSet.as_view({'get':'list'})) #get all campaigns
]

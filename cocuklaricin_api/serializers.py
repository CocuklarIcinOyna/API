from rest_framework import serializers
from .models import Machine, Fund, Campaign

class MachineSerializer(serializers.ModelSerializer):
    total_fund = serializers.IntegerField()
    class Meta:
        model = Machine
        fields = ['nick_name','address','map_url','campaign','total_fund']

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['amount','is_canceled','time','machine','cancel_time']

class CampaignSerializer(serializers.ModelSerializer):
    #machines = Campaign.machine.filter(active=True)
    class Meta:
        model = Campaign
        fields = ['start_date','end_date','description','machines']

from rest_framework import serializers
from .models import Machine, Fund, Campaign

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['nick_name','address','map_url','campaign','fund']

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['amount','is_canceled','time']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['start_date','end_date','description']

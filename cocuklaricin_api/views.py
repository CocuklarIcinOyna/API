from django.shortcuts import render, get_object_or_404
from .models import Machine, Fund, Campaign

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import MachineSerializer, FundSerializer, CampaignSerializer

class MachineView(APIView):
    def get(self, request, pk):
        try:
            machine = Machine.objects.get(pk=pk, active=True)
        except Machine.DoesNotExist:
            machine = []
        serializer = MachineSerializer(machine, many=False)
        return Response({"machine": serializer.data})

    def delete(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        machine.delete()
        return Response({"success":"Machine %s [%s] updated successfully" % (machine.nick_name, machine.pk)})

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.filter(active=True)
    serializer_class = MachineSerializer

class FundView(APIView):
    '''
    This endpoint is used by arcade machines
    '''
    def get(self, request, pk):
        fund = get_object_or_404(Fund, pk=pk)
        serializer = FundSerializer(fund, many=False)
        return Response({'fund':serializer.data})

    def post(self, request):
        data = request.data.get('fund')
        serializer = FundSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            fund_saved = serializer.save()
        return Response({'success':'Fund is saved successfully','fund_id':fund_saved.pk})

    def put(self,request, pk):
        fund = get_object_or_404(Fund, pk=pk)
        data = request.data.get('fund')
        serializer = FundSerializer(instance=fund, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_fund = serializer.save()
        return Response({'success':'Fund is updated successfully','fund_id':updated_fund.pk})

class CampaignView(APIView):
    def get(self,request,pk):
        campaign = get_object_or_404(Campaign, pk=pk, active=True)
        serializer = CampaignSerializer(campaign, many=False)
        return Response({'campaign':serializer.data})

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.filter(active=True)
    serializer_class = CampaignSerializer

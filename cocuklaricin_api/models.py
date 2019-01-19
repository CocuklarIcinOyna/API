from django.db import models

class Machine(models.Model):
    nick_name = models.CharField(blank=True, max_length=200)
    address = models.CharField(blank=False, null=False, max_length=1000)
    map_url = models.URLField(blank=False, null=False)
    fund_raise_date = models.DateField(blank=False, null=False)
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    fund = models.ForeignKey('fund', on_delete=models.SET_NULL,blank=True, null=True)

class Fund(models.Model):
    amount = models.FloatField(blank=False)
    cancel_time = models.DateTimeField(blank=True, null=True)
    time = models.DateTimeField(blank=False, null=False)
    is_canceled = models.BooleanField(default=False)

class Campaign(models.Model):
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    description = models.TextField(max_length=3000)
    notes = models.TextField(blank=True)

class CompanyExecutive(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    surname = models.CharField(blank=False, null=False, max_length=15)
    gsm_no = models.CharField(blank=False, null=False, max_length=25)
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)

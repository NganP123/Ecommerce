from __future__ import unicode_literals
from django.db import models

class ShipmentStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name

class Shipment(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)  # corrected field name
    email = models.CharField(max_length=50)  # corrected field definition
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    shipment_fee = models.IntegerField(default=40000)
    shipment_status_id = models.IntegerField(default=1)  # corrected field name and definition

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s ' % (self.fname, self.lname, self.email, self.mobile, self.address, self.shipment_fee, self.shipment_status_id)

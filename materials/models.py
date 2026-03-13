from django.db import models
from masters.models import *
class MaterialMaster(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    work_spots = models.ForeignKey(WorkSpots,on_delete=models.CASCADE)

    description = models.CharField(max_length=200)

    units = models.ForeignKey(UnitMaster,on_delete=models.CASCADE)

    quantity = models.IntegerField()

    qty = models.IntegerField()

    rate = models.FloatField()

    rackno = models.CharField(max_length=50)

    critical_qty = models.IntegerField()

    photo = models.ImageField(upload_to="materials")

    added_on = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=True)
class MaterialReceipt(models.Model):

    issue_date = models.DateField()

    entry_no = models.IntegerField()

    challan_no = models.CharField(max_length=50)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    item = models.ForeignKey(MaterialMaster,on_delete=models.CASCADE)

    totalno = models.IntegerField()

    rate = models.FloatField()

    rackno = models.CharField(max_length=50)

    total_stock = models.IntegerField()

    receive_from = models.CharField(max_length=200)

    vehicle_no = models.CharField(max_length=50)

    receiver = models.CharField(max_length=100)

    remarks = models.TextField()

class MaterialRequisition(models.Model):

    issue_date = models.DateField()

    entry_no = models.IntegerField()

    requisition_no = models.CharField(max_length=50)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    work_spots = models.ForeignKey(WorkSpots,on_delete=models.CASCADE)

    item = models.ForeignKey(MaterialMaster,on_delete=models.CASCADE)

    total_nos = models.IntegerField()

    requisition_by = models.CharField(max_length=100)

    remarks = models.TextField()

class MaterialOutward(models.Model):

    issue_date = models.DateField()

    entry_no = models.IntegerField()

    location = models.CharField(max_length=100)

    contents = models.CharField(max_length=100)

    contents2 = models.CharField(max_length=100)

    description = models.TextField()

    totalno = models.IntegerField()

    vendor = models.CharField(max_length=100)

    issuedto = models.CharField(max_length=100)

    vehicleno = models.CharField(max_length=50)

    purpose = models.CharField(max_length=200)

    issuer = models.CharField(max_length=100)

    returnable = models.BooleanField(default=False)

    remarks = models.TextField()

    acknowledgement = models.BooleanField(default=False)
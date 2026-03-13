from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100)
    def __str__(self):
        return self.sub_category


class UnitMaster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name



class TypeOfSeller(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.type


class WorkSpots(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class PartyMaster(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
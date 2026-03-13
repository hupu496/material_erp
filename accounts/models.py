from django.db import models

class Category(models.Model):

    name=models.CharField(max_length=100)

    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    sub_category=models.CharField(max_length=100)


class UnitMaster(models.Model):

    name=models.CharField(max_length=50)

    status=models.BooleanField(default=True)


class WorkSpots(models.Model):

    name=models.CharField(max_length=100)

    status=models.BooleanField(default=True)


class TypeOfSeller(models.Model):

    type=models.CharField(max_length=100)

    status=models.BooleanField(default=True)


class PartyMaster(models.Model):

    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    type=models.CharField(max_length=50)

    name=models.CharField(max_length=200)

    address=models.TextField()

    phone=models.CharField(max_length=20)

    email=models.EmailField()

    added_on=models.DateTimeField(auto_now_add=True)

    status=models.BooleanField(default=True)
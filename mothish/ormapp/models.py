from django.db import models
from django.contrib import admin
class product(models.Model):
    product_Name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    Category=models.CharField(max_length=100 )
    Date_Of_Manufacture=models.DateField()
    Colour=models.CharField(max_length=50)
    price=models.FloatField()
    

class productAdmin(admin.ModelAdmin):
    list_display=["product_Name","product_id","price","Colour","Date_Of_Manufacture","Category"]
# Create your models here#
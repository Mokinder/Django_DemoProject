from django.db import models

# Create your models here.

class productcategory(models.Model):
    category_num=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50, help_text="Enter category name ",verbose_name='Category name')

class product(models.Model):
    product_num=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,help_text='Enter product name',verbose_name='Product name')
    product_category=models.ForeignKey('productcategory',on_delete=models.SET_NULL,null=True)
    product_price=models.FloatField()

class bill(models.Model):
    bill_num=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50,help_text='enter the customer name',verbose_name="Customer Name")
    products=models.ManyToManyField('product')
    total_sum=models.FloatField()


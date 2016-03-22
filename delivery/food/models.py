from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    '''
        Will store the details related to customers
    '''
    user_id = models.ForeignKey(User)
    address = models.CharField(null=True,
                               max_length=500)
    phone = models.CharField(null=True,
                             max_length=30)
    reg_date = models.CharField(null=True,
                                max_length=20)

class Resturant(models.Model):
    '''
        Will store the details related to resturant
    '''
    owner_id = models.ForeignKey(User)
    resturant_address = models.CharField(null=True, max_lenght=500)
    opening_time = models.CharField(null=True, max_length=20)
    closing_time = models.CharField(null=True, max_length=20)


class MenuItems(models.Model):
    '''
        Store the details related to items in the menu
    '''
    item_name = models.CharField(max_length=20)
    price = models.IntegerField(max_length=20)
    item_description = models.CharField(max_length=500)
    item_category = models.CharField(max_length=50)
    resturant_id = models.ForeignKey(Resturant)


class Order(models.Model):
    '''
        Store the details related to order
    '''


class Invoice(models.Model):
    '''
        Store the details related to invoice
    '''

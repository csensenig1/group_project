from django.db import models
from django.urls import reverse


class RequestContact(models.Model):
    cont_ID = models.CharField(max_length=50)
    cont_Fname = models.CharField(max_length=200)
    cont_Lname = models.CharField(max_length=200)
    cont_preferredService = models.CharField(max_length=200)


class Service(models.Model):
    serv_id = models.CharField(max_length=50)
    serv_title = models.CharField(max_length=200)
    serv_info = models.CharField(max_length=200)
    serv_cost = models.CharField(max_length=200)


class Invoice(models.Model):
    Inv_no = models.CharField(max_length=50)
    Inv_date = models.CharField(max_length=200)
    Inv_total = models.CharField(max_length=200)
    Inv_description = models.CharField(max_length=200)

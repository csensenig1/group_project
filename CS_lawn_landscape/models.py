from django.db import models
from django.urls import reverse


class RequestContact(models.Model):
    cont_ID = models.CharField(max_length=50)
    cont_first_name = models.CharField(max_length=200)
    cont_last_name = models.CharField(max_length=200)
    cont_preferredService = models.CharField(max_length=200)


class UserReview(models.Model):
    rev_id = models.ForeignKey('Review', on_delete=models.RESTRICT, null=True)


class Review(models.Model):
    rev_id = models.CharField(max_length=50)
    rev_rating = models.CharField(max_length=5)
    rev_comments = models.CharField(max_length=500)
    serv_id = models.ForeignKey('Service', on_delete=models.RESTRICT, null=True)


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
    serv_id = models.ForeignKey('Service', on_delete=models.RESTRICT, null=True)


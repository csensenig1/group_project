from django.db import models
from django.urls import reverse


class Service(models.Model):
    serv_id = models.CharField(max_length=50)
    serv_title = models.CharField(max_length=200)
    serv_info = models.CharField(max_length=200)
    serv_cost = models.CharField(max_length=200)

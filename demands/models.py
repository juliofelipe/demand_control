from django.db import models
from django.contrib.auth.models import User


class Demandant(models.Model):
  demandant_name = models.CharField(max_length=25, null=True, blank=True)

  def __str__(self):
    return self.demandant_name


class Channel(models.Model):
  channel_name = models.CharField(max_length=25, null=True, blank=True)

  def __str__(self):
    return self.channel_name


class Demand(models.Model):
  request_date = models.DateField(null=True, blank=True)
  completion_date = models.DateField(null=True, blank=True)
  demand = models.TextField()
  image = models.ImageField(upload_to='demandas_photos', null=True, blank=True)
  demandant = models.ManyToManyField( Demandant, blank=True)
  assignment = models.ForeignKey( User,on_delete=models.PROTECT)
  channel = models.ForeignKey(Channel, on_delete=models.PROTECT)
  note = models.TextField(null=True, blank=True)
  effective_date_completion = models.DateField('Data efetiva da conclusão', null=True, blank=True)

  def __str__(self):
    return self.demand





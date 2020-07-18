from django.db import models
from django.contrib.auth.models import User


class Demandante(models.Model):
  nome_damandante = models.CharField(max_length=25, null=True, blank=True)

  def __str__(self):
    return self.nome_damandante


class Canal(models.Model):
  nome_canal = models.CharField(max_length=25, null=True, blank=True)

  def __str__(self):
    return self.nome_canal


class Demanda(models.Model):
  data_solicitacao = models.DateField(null=True, blank=True)
  data_conclusao = models.DateField(null=True, blank=True)
  demanda = models.TextField()
  image = models.ImageField(upload_to='demandas_photos', null=True, blank=True)
  demandante = models.ManyToManyField('Demandante', blank=True)
  atribuicao = models.ForeignKey(User,on_delete=models.PROTECT)
  canal = models.ForeignKey(Canal, on_delete=models.PROTECT)
  observacoes = models.TextField(null=True, blank=True)
  data_efetiva_conclusao = models.DateField(null=True, blank=True)

  def __str__(self):
    return self.demanda





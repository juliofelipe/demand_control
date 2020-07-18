from django.shortcuts import render
from .models import Demanda


def demanda_list(request):
  demandas = Demanda.objects.all()
  return  render(request, 'demandas.html', {'demandas': demandas})

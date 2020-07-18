from django.shortcuts import render, redirect, get_object_or_404
from .models import Demand
from .forms import DemandForm


def demand_list(request):
  demands = Demand.objects.all()
  return  render(request, 'demands/demand_list.html', {'demands': demands})


def demand_new(request):
  form = DemandForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('demand_list')

  return render(request, 'demands/demand_form.html', {'form': form})


def demand_update(request, id):
  demand = get_object_or_404(Demand, pk=id)
  form = DemandForm(request.POST or None, request.FILES or None, instance=demand)

  if form.is_valid():
    form.save()
    return redirect('demand_list')

  return render(request, 'demands/demand_form.html', {'form': form})


def demand_delete(request, id):
  demand = get_object_or_404(Demand, pk=id)
  form = DemandForm(request.POST or None, request.FILES or None, instance=demand)

  if request.method == 'POST':
    demand.delete()
    return redirect('demand_list')
  
  return render(request, 'demands/demand_delete_confirm.html', {'demand': demand })
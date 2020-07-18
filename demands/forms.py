from django.forms import ModelForm
from .models import Demand

class DemandForm(ModelForm):

  class Meta:
    model = Demand
    fields = ['id', 'request_date', 'completion_date', 'demand', 'image', 'demandant', 'assignment', 'channel', 'note' , 'effective_date_completion',]


 
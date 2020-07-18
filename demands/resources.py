from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from demands.models import Demand, Demandant

class DemandResource(resources.ModelResource):
    demandant=fields.Field(attribute='demandant', widget=ManyToManyWidget(Demandant, field='damandant_name'))
    
    class Meta:
        model = Demand
        fields = ('id', 'request_date', 'completion_date', 'demand', 'demandant', 'channel', 'note' , 'effective_date_completion',)



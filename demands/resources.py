from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from demands.models import Demanda, Demandante

class DemandaResource(resources.ModelResource):
    demandante=fields.Field(attribute='demandante', widget=ManyToManyWidget(Demandante, field='nome_damandante'))
    
    class Meta:
        model = Demanda
        fields = ('id', 'data_solicitacao', 'data_conclusao', 'demanda', 'demandante', 'canal', 'observacoes' , 'data_efetiva_conclusao',)
from django.contrib import admin
from .models import Demanda, Demandante, Canal
from import_export.admin import ImportExportModelAdmin
from .resources import DemandaResource


class DemandaAdmin(ImportExportModelAdmin):
    resource_class = DemandaResource

admin.site.register(Demanda, DemandaAdmin)
admin.site.register(Demandante)
admin.site.register(Canal)
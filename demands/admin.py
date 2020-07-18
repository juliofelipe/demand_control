from django.contrib import admin
from .models import Demand, Demandant, Channel
from import_export.admin import ImportExportModelAdmin
from .resources import DemandResource


class DemandAdmin(ImportExportModelAdmin):
    resource_class = DemandResource

admin.site.register(Demand, DemandAdmin)
admin.site.register(Demandant)
admin.site.register(Channel)
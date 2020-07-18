from django.urls import path
from .views import demand_list, demand_new, demand_update, demand_delete

urlpatterns = [
  path('list/', demand_list, name="demand_list"),
  path('new/', demand_new, name="demand_new"),
  path('update/<int:id>/', demand_update, name="demand_update"),
  path('delete/<int:id>/', demand_delete, name="demand_delete")
]
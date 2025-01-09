from django.contrib import admin
from . import models

class ViewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(models.guide_types_of_maintenance, ViewsAdmin)
admin.site.register(models.guide_recovery_method, ViewsAdmin)
admin.site.register(models.guide_failure_node, ViewsAdmin)
admin.site.register(models.guide_technique_model, ViewsAdmin)
admin.site.register(models.guide_engine_model, ViewsAdmin)
admin.site.register(models.guide_transmission_model, ViewsAdmin)
admin.site.register(models.guide_model_drive_bridge, ViewsAdmin)
admin.site.register(models.guide_model_controlled_bridge, ViewsAdmin)
admin.site.register(models.machine)
admin.site.register(models.maintenance)
admin.site.register(models.reclamation)

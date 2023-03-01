from django.contrib import admin

from .models import Donate, Petition_for_legal_entity, Petition_for_physical_entity

admin.site.register(Donate)
admin.site.register(Petition_for_legal_entity)
admin.site.register(Petition_for_physical_entity)


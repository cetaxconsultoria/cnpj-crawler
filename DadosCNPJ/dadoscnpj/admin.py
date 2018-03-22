from django.contrib import admin
from .models import *

class CNPJAdmin(admin.ModelAdmin):
    fieldsets = [
            ('CNPJ-Id', {'fields': ['cnpj']}),
            ('Atributes', {'fields': ['attrs']}),]

admin.site.register(CNPJ, CNPJAdmin)

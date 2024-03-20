from django.contrib import admin
from .models import *

# Register your models here.

class ProyectoFotoAdmin(admin.TabularInline):
    model = ProyectoFotos

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","email","edad"]
    search_fields = ["nombre","apellido","email"]
    list_per_page = 20

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre','tipo','comercial']
    list_editable = []
    search_fields = ['nombre','tipo']
    list_filter = ['comercial']
    list_per_page = 10
    inlines = [
        ProyectoFotoAdmin
    ]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","tipo_consulta","mensaje"]
    search_fields = ["nombre","email"]
    list_filter = ["tipo_consulta"]





admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(ProyectoFotos)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Avatar)
#-*- encoding: utf-8 -*-

from django.contrib import admin
from proyecto.app import models

class ItemPreguntaEnLinea(admin.StackedInline):
    model = models.ItemPregunta
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ItemPreguntaEnLinea]
    fields = ('texto','orden','tipo','seccion')

class PreguntaEnLinea(admin.TabularInline):
    model = models.Pregunta
    extra = 1

class SeccionEnLinea(admin.TabularInline):
    model = models.Seccion
    extra = 1

class SeccionAdmin(admin.ModelAdmin):
    inlines = [PreguntaEnLinea]
    fields = ('titulo','descripcion','orden','cuestionario','seccionPadre')

class CuestionarioAdmin(admin.ModelAdmin):
    inlines = [SeccionEnLinea]
    save_as = True

class OfertaAcademicaSGAEnLinea(admin.TabularInline):
    model = models.OfertaAcademicaSGA
    extra = 1

class PeriodoEvaluacionEnLinea(admin.StackedInline):
    model = models.PeriodoEvaluacion
    extra = 1

class PeriodoAcademicoAdmin(admin.ModelAdmin):
    inlines = (PeriodoEvaluacionEnLinea,)
    filter_horizontal = ('ofertasAcademicasSGA',)


class EstudiantePeriodoAcademicoAsignaturaEnLinea(admin.TabularInline):
    model = models.EstudiantePeriodoAcademicoAsignatura
    extra = 3
    verbose_name = 'Asignaturas Estudiante'
    raw_id_fields = ("asignatura",)


class EstudiantePeriodoAcademicoAdmin(admin.ModelAdmin):
    inlines = [EstudiantePeriodoAcademicoAsignaturaEnLinea]
    raw_id_fields = ('estudiante',)
    

class DocentePeriodoAcademicoAsignaturaEnLinea(admin.TabularInline):
    model = models.DocentePeriodoAcademicoAsignatura
    extra = 3
    verbose_name = 'Asignaturas Docente'
    raw_id_fields = ("asignatura",)

    
class DocentePeriodoAcademicoAdmin(admin.ModelAdmin):
    inlines = (DocentePeriodoAcademicoAsignaturaEnLinea,)
    raw_id_fields = ('docente',)

    
class AsignaturaAdmin(admin.ModelAdmin):
    search_fields = ('area','carrera','semestre','paralelo','nombre',)
    list_filter = ('area','carrera','semestre','paralelo','tipo','nombre',)
    #TODO: combobox
    #readonly_fields = ('area','carrera','semestre','paralelo','tipo',)
    fieldsets = (
        ('Datos Académicos', {
            'fields': ('area', 'carrera', 'semestre', 'paralelo')
            }),
        ('Asignatura', {
            'fields': ('nombre', 'tipo', 'creditos', 'duracion')
            }),        
        )
    

class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('username','cedula')


admin.site.register(models.Cuestionario,CuestionarioAdmin)
admin.site.register(models.Seccion,SeccionAdmin)
admin.site.register(models.Pregunta,PreguntaAdmin)
admin.site.register(models.PeriodoAcademico,PeriodoAcademicoAdmin)
admin.site.register(models.EstudiantePeriodoAcademico, EstudiantePeriodoAcademicoAdmin)
admin.site.register(models.DocentePeriodoAcademico, DocentePeriodoAcademicoAdmin)
admin.site.register(models.Asignatura, AsignaturaAdmin)
admin.site.register(models.Usuario, UsuarioAdmin)


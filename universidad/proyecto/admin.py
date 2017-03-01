from django.contrib import admin

from .models import Alumnos, Profesores, Materias, Licenciaturas

@admin.register(Alumnos)
class AdminAlumnos(admin.ModelAdmin):
	list_display = ('name','age','semestre','licenciatura',)

@admin.register(Profesores)
class AdminProfesores(admin.ModelAdmin):
	list_display = ('name','age','especialidad',)

@admin.register(Materias)
class AdminMaterias(admin.ModelAdmin):
	list_display = ('name','semestre','licenciatura',)

@admin.register(Licenciaturas)
class AdminLicenciaturas(admin.ModelAdmin):
	list_display = ('name',)

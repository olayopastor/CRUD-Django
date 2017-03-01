from django import forms
from .models import Alumnos, Profesores, Materias
class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('name', 'age', 'semestre', 'licenciatura')

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ('name', 'age', 'especialidad')

class MateriasForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ('name', 'semestre', 'licenciatura')

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('name',)

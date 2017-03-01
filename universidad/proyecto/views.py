
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Alumnos, Profesores, Materias, Licenciaturas
from .forms import AlumnosForm, ProfesoresForm, MateriasForm

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))

def mat_disp(request):
    template = loader.get_template('mat_disp.html')
    return HttpResponse(template.render(request))

def mat_vista(request):
    alumnoss = Alumnos.objects.all()
    template = loader.get_template('mat_vista.html')
    context = {
        'title': 'alumnoss',
        'alumnoss': alumnoss,
    }
    return HttpResponse(template.render(context, request))

class AlumnosListView(ListView):
    model = Alumnos
    template_name = "alu_vista.html"

class AlumnosDetailView(DetailView):
    model = Alumnos
    template_name = "alu_detail.html"

class AlumnosCreateView(CreateView):
    model = Alumnos
    fields = ['name','semestre','licenciatura','photo']
    template_name = "alu_new.html"

    def get_success_url(self):
        return reverse('alu_vista')

class AlumnosDeleteView(DeleteView):
    model = Alumnos
    success_url = reverse_lazy('alu_vista')
    template_name ="alu_confirm_delete.html"

class AlumnosUpdateView(UpdateView):
    model = Alumnos
    fields = ['name','age','semestre','licenciatura','photo']
    template_name = "alu_new.html"
    success_url = reverse_lazy('alu_vista')

# Class Profesores

class ProfesoresListView(ListView):
    model = Profesores
    template_name = "pro_vista.html"

class ProfesoresDetailView(DetailView):
    model = Profesores
    template_name = "pro_detail.html"

class ProfesoresCreateView(CreateView):
    model = Profesores
    fields = ['name','age','especialidad','photo']
    template_name = "pro_new.html"

    def get_success_url(self):
        return reverse('pro_vista')

class ProfesoresDeleteView(DeleteView):
    model = Profesores
    success_url = reverse_lazy('pro_vista')
    template_name ="pro_confirm_delete.html"

class ProfesoresUpdateView(UpdateView):
    model = Profesores
    fields = ['name','age','especialidad','photo']
    template_name = "pro_new.html"
    success_url = reverse_lazy('pro_vista')

#Class Materias

# class MateriasListView(ListView):
#     model = Materias
#     template_name = "alu_vista2.html"

class MateriasUpdateView(UpdateView):
    model = Alumnos
    fields = ['age']
    template_name = "mat_asig.html"
    success_url = reverse_lazy('alu_vista')

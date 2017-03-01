from __future__ import unicode_literals

from django.db import models

class Licenciaturas(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Alumnos(models.Model):
	name = models.CharField(max_length=200)
	age = models.CharField(max_length=200)
	semestre = models.IntegerField(default=0)
	#materia = models.CharField(max_length=100)
	licenciatura = models.ForeignKey(Licenciaturas)
	photo = models.ImageField(blank=True)

class Profesores(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	especialidad = models.CharField(max_length=200)
	photo = models.ImageField(blank=True)

class Materias(models.Model):
	name = models.CharField(max_length=200)
	semestre = models.IntegerField(default=0)
	licenciatura = models.ForeignKey(Licenciaturas)

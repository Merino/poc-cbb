from django.db import models

# Create your models here.

class NestedA(models.Model):
    name = models.CharField(max_length=30)

class NestedB(models.Model):
    nested_a = models.ForeignKey('NestedA')
    name = models.CharField(max_length=30)

class NestedC(models.Model):
    nested_b = models.ForeignKey('NestedB')
    name = models.CharField(max_length=30)

class NestedD(models.Model):
    nested_c = models.ForeignKey('NestedC')
    name = models.CharField(max_length=30)
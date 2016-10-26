from django.db import models

from panels.fields import RichTextarea


class ListData(models.Model):
    """
        Model to demonstrate the ListView
    """
    name = models.CharField(max_length=50, help_text='Get a unique name')
    date = models.DateField()
    datetime = models.DateTimeField()
    decimal = models.DecimalField(decimal_places=2, max_digits=5)
    boolean = models.BooleanField(default=True, help_text='True or False')
    select = models.CharField(choices=[('10', '10'), ('20', '20'), ('30', 'Dertig'), ('40', '40')], default=40, max_length=8)

    description = RichTextarea(null=False, blank=True)

    def __unicode__(self):
        return self.name

"""
    Model to demonstrate the inlines
"""

class GlobalA(models.Model):
    name = models.CharField(max_length=30)

class GlobalB(models.Model):
    name = models.CharField(max_length=30)


class NestedA(models.Model):
    name = models.CharField(max_length=30)
    global_a = models.ForeignKey('GlobalA', null=True, blank=True)
    decimal = models.DecimalField(decimal_places=2, max_digits=5)
    boolean = models.BooleanField(default=True)


class NestedB1(models.Model):
    nested_a = models.ForeignKey('NestedA')
    global_b = models.ForeignKey('GlobalB', null=True, blank=True)
    name = models.CharField(max_length=30)


class NestedB2(models.Model):
     nested_a = models.ForeignKey('NestedA')
     name = models.CharField(max_length=30)


class NestedC1(models.Model):
     nested_b = models.ForeignKey('NestedB1')
     name = models.CharField(max_length=30)


class NestedC2(models.Model):
     nested_b = models.ForeignKey('NestedB1')
     name = models.CharField(max_length=30)


class NestedC3(models.Model):
     nested_b = models.ForeignKey('NestedB2')
     name = models.CharField(max_length=30)
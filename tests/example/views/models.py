from django.db import models


class ListData(models.Model):
    """
        Model to demonstrate the ListView
    """
    name = models.CharField(max_length=50)
    date = models.DateField()
    datetime = models.DateTimeField()
    decimal = models.DecimalField(decimal_places=2, max_digits=5)
    boolean = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

"""
    Model to demonstrate the inlines
"""
class NestedA(models.Model):
    name = models.CharField(max_length=30)
    decimal = models.DecimalField(decimal_places=2, max_digits=5)
    boolean = models.BooleanField(default=True)


class NestedB1(models.Model):
     nested_a = models.ForeignKey('NestedA')
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
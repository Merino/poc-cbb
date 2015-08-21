from django.db import models

# Create your models here.

class ListData(models.Model):
    """
        Model to demonstrate the ListView
    """
    name = models.CharField(max_length=50)
    date = models.DateField()
    datetime = models.DateTimeField()
    decimal = models.DecimalField(decimal_places=2, max_digits=5)
    boolean = models.BooleanField(default=True)


# class NestedA(models.Model):
#     name = models.CharField(max_length=30)
#
# class NestedB(models.Model):
#     nested_a = models.ForeignKey('NestedA')
#     name = models.CharField(max_length=30)
#
# class NestedC(models.Model):
#     nested_b = models.ForeignKey('NestedB')
#     name = models.CharField(max_length=30)
#
# class NestedD(models.Model):
#     nested_c = models.ForeignKey('NestedC')
#     name = models.CharField(max_length=30)
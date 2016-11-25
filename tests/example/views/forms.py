from django import forms

from vesper.widgets import InputWidget, RadioSelectWidget

CHOICES = [
    ('1', 'Value 1'),
    ('2', 'Value 2'),
    ('3', 'Value 3'),
]

class FieldsForm(forms.Form):
    input = forms.CharField(required=True, widget=InputWidget)
    select = forms.ChoiceField(choices=CHOICES, required=True)
    radio = forms.ChoiceField(choices=CHOICES, widget=RadioSelectWidget, required=True)
    check = forms.BooleanField(required=True)
    textarea = forms.CharField(widget=forms.Textarea)
    #date = forms.DateField(required=True)
    email = forms.EmailField(required=True)


class CreateShipmentForm(forms.Form):
    channel = forms.ChoiceField(choices=[], widget=RadioSelectWidget, required=True)
    shipment_method = forms.ChoiceField(choices=[], widget=RadioSelectWidget, required=True)
    shipment_number = forms.CharField(max_length=100, required=False)
    parcels = forms.IntegerField(initial=1, required=True, help_text='Number of parcels')
    reference = forms.CharField(max_length=100, required=False, initial=None, help_text='If empty copies reference from each order')
    print_labels = forms.BooleanField(initial=True, required=False, help_text='Print label after creating a shipment')

    def __init__(self, *args, **kwargs):
        choices_channel = kwargs.pop('choices_channel')
        choices_shipment_method = kwargs.pop('choices_shipment_method')

        super(CreateShipmentForm, self).__init__(*args, **kwargs)

        self.fields['channel'].choices = choices_channel
        self.fields['shipment_method'].choices = choices_shipment_method


class CreatePackageForm(forms.Form):
    BOX = 'BOX'
    PALLET = 'PALLET'

    TYPE = (
        (BOX, 'Pakket'),
        (PALLET, 'Pallet'),
    )

    type = forms.ChoiceField(choices=TYPE, initial=BOX)

    # Measurements
    length = forms.IntegerField(required=True, help_text='gemeten in cm')
    width  = forms.IntegerField(required=True, help_text='gemeten in cm')
    height = forms.IntegerField(required=True, help_text='gemeten in cm')
    weight = forms.IntegerField(required=True, help_text='gemeten in kg')
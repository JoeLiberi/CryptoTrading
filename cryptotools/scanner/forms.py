from django import forms

class ScanForm(forms.Form):
    percent_increase = forms.IntegerField(label='Percent Volume Increase')
    num_bars = forms.IntegerField(label='Number of Bars', max_value=5)


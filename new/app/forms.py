from django import forms

class input(forms.Form):
    s_name=forms.CharField(label='NAME',max_length=50)
    s_roll = forms.CharField(label='ROLL', max_length=10)
    s_sec = forms.CharField(label='SEC', max_length=2)
    s_CGPA=forms.CharField(label='CGPA',max_length=2)
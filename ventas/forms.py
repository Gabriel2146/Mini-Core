from django import forms

class FiltroFechaForm(forms.Form):
    fecha_inicio = forms.DateField(label="Fecha inicio", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(label="Fecha fin", widget=forms.DateInput(attrs={'type': 'date'}))

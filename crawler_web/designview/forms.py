from django import forms


class MainSearchForm(forms.Form):
    name = forms.CharField(max_length=100)
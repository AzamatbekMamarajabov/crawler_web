from django import forms


class MainSearchForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                
                'id': 'price',
                
                'placeholder': 'Name ',
                'class': 'form-control rounded-pill px-4',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    
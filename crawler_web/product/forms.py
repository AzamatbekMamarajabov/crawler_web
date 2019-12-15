from django import forms
from .models import ProductModel, CarModel


class ProductForm(forms.ModelForm):

    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={

                'id': 'name',

                'placeholder': 'name ',
                'class': 'form-control  rounded-pill mx-3 ',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    year = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={

                'id': 'year',

                'placeholder': 'year ',
                'class': 'form-control  rounded-pill  mx-3 ',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    region = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={

                'id': 'region',

                'placeholder': 'region ',
                'class': 'form-control  rounded-pill  mx-3 ',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    price = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={

                'id': 'price',

                'placeholder': 'price ',
                'class': 'form-control  rounded-pill  mx-3 ',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductTopForm(forms.ModelForm):

    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Search Posts ',
                'class': 'form-control ',
                'autocomplete': 'off',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Search Posts"',

            }
        ),
        required=False,
    )

    class Meta:
        model = ProductModel
        fields = ('name',)


class CarTopForm(forms.ModelForm):

    car_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Search Posts ',
                'class': 'form-control ',
                'autocomplete': 'off',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Search Posts"',

            }
        ),
        required=False,
    )

    class Meta:
        model = CarModel
        fields = ('car_name',)

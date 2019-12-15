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




WEBSITE_CHOICES = [
    ('olx.uz', 'olx.uz'),
    ('avtoelon.uz', 'avtoelon.uz'),
    ('avtobor.uz', 'avtobor'),
]



class CarTopForm(forms.ModelForm):

    car_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Name',
                'class': 'form-control ',
                'autocomplete': 'off',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Search Posts"',

            }
        ),
        required=False,
    )

    car_year = forms.CharField(
        
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'min year',
                'class': 'form-control ',
                'default': '0',
                
            }
        ),
        required=False,
    )

    website = forms.MultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'type': 'text',
                
            }
        ),
        choices=WEBSITE_CHOICES,
        required=False,
    )

    price_bottom = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                
                'placeholder': 'min price ',
                'class': 'form-control  rounded-pill  mx-3 ',
                'autocomplete': 'off',

            }
        ),
        required=False,
    )

    price_top = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={

                'id': 'price',

                'placeholder': 'max price ',
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



    class Meta:
        model = CarModel
        fields = ('car_name','car_year', 'region','price_bottom', 'price_top',)

class CarWebForm(forms.ModelForm):



    website = forms.MultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'type': 'text',
                'placeholder': 'Search Posts ',
                'class': 'form-control ',
                'autocomplete': 'off',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Search Posts"',

            }
        ),
        choices=WEBSITE_CHOICES,
        required=False,
    )



    class Meta:
        model = CarModel
        fields = ('website',)

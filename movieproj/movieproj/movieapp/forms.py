from django import forms
class SearchForm(forms.Form):
    search=forms.CharField(label='Search for Movies..',max_length=100)

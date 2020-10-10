from django import forms

class GetMovies(forms.Form):
    url = forms.URLField()
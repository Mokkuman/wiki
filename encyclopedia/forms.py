from django import forms 

class newPageForm(forms.Form):
    titulo = forms.CharField(label='Title', max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)
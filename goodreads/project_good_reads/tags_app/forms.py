from django import forms

class TagForm(forms.Form):
    tag_name = forms.CharField(label='Tag name')
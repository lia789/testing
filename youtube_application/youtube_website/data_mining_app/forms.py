from django import forms
from .models import ChannelSearchKeyword, DataToCSV



class ChannelSearchKeywordForm(forms.ModelForm):
    class Meta:
        model = ChannelSearchKeyword
        # fields = ["channel_keyword"]
        fields = "__all__"



class DataToCSVForm(forms.ModelForm):
    class Meta:
        model = ChannelSearchKeyword
        fields = "__all__"



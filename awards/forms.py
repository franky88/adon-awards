from django import forms
from django.forms import RadioSelect, widgets, TextInput
from .models import Awardee, AwardTitle, CertBG


class AddAwardeeForm(forms.ModelForm):
    class Meta:
        model = Awardee
        fields = [
            "award_title",
            "name",
            "date",
            "citation",
            # "gender",
            "background"
        ]
        widgets = {
            'date': TextInput(attrs={'type': 'date'})
        }


class AddAwardeeTitleForm(forms.ModelForm):
    class Meta:
        model = AwardTitle
        fields = [
            "title",
        ]


class AddBackgroundForm(forms.ModelForm):
    class Meta:
        model = CertBG
        fields = [
            "name",
            "background"
        ]

from django import forms

from todo.models import todo


class todoform(forms.ModelForm):
    class Meta:
        model =todo
        fields ="__all__"
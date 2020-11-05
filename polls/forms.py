from django import forms


class Acquire(forms.Form):
    username = forms.CharField(required=True)  # required=True必填字段
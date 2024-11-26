from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

class PrimeNumbersForm(forms.Form):
    start = forms.IntegerField()
    stop = forms.IntegerField()

class SubscriptionForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
from django import forms
from .models import CATEGORY

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
        #self.fields['submit'].widget.attrs['id'] = 'submit'

    username = forms.CharField(label='Username', max_length=32, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class ServiceLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ServiceLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Company Name', max_length=32, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Username', max_length=20, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput, required=True)

class ServiceSignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ServiceSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['address'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Company Name', max_length=20, required=True)
    address = forms.CharField(label='Address', max_length=256, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput, required=True)

class ServiceCodeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ServiceCodeForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update({
            'autocomplete': 'off'
        })

    code = forms.IntegerField(label='Code', required=True)

class CreateEventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['item'].widget.attrs.update({
            'autocomplete': 'off'
        })

    item = forms.CharField(label='Item: ', required=True)
    amount = forms.IntegerField(label='Stock Left:', required=True)
    category = forms.ChoiceField(label='Amount: ', choices=CATEGORY, required=True)
    start_time = forms.TimeField(label='Start Time(HH:MM): ', widget=forms.TimeInput(format='%H:%M'), required=True)
    end_time = forms.TimeField(label='End Time(HH:MM): ', widget=forms.TimeInput(format='%H:%M'), required=True)
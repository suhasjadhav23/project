# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class MyRegistrationForm(UserCreationForm):
# -------------------------------------------
#     # email = forms.EmailField(required=True)
#     #
#     # class Meta:
#     #     model = User
#     #     fields = ( 'username', 'email', 'password1', 'password2')
#
#
#     def save(self, commit=True):
#         user = super(MyRegistrationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         # user.set_password(self.cleaned_data['password1'])
#
#         if commit:
#             user.save()
#
#         return user
#
#
# # to be continued
# # class ContactForm1(forms.Form):
# #     subject = forms.CharField(max_length=100)
# #
# # class ContactForm2(forms.Form):
# #     sender = forms.EmailField()
# #
# # class ContactForm3(forms.Form):
# #     message = forms.CharField(widget=forms.Textarea)
#
#
# -----------------------------------------------------------------------------------------------------------------------
# attempt to use email verification sysytem
# -----------------------------------------------------------------------------------------------------------------------
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


def clean_email(self):
    email = self.cleaned_data["email"]
    try:
        User._default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('duplicate email')

    #modify save() method so that we can set user.is_active to False when we first create our user


def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.is_active = False  # not active until he opens activation link
        user.save()

    return user
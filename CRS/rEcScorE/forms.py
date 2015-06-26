# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class MyRegistrationForm(UserCreationForm):
# -------------------------------------------
# # email = forms.EmailField(required=True)
# #
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
# import datetime
# from django.utils import timezone
from django.forms import DateTimeField


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        User = (User.objects.all().order_by('first_name', 'last_name', 'username'))
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


# ------------------------------------------------------------------------------------------------------------------------------
# Update/ Fill Profile of Employee
# ------------------------------------------------------------------------------------------------------------------------------
from models import *

class EmpProf(forms.ModelForm):
    # your_name = forms.CharField(label='Your name :', max_length=100)
    # dob = forms.DateTimeField(label='Date Of Birth :')
    # city = forms.CharField(label='City :', max_length=50)
    # country = forms.CharField(label='Country :', max_length=50)
    # highest_degree = forms.CharField(label='Qualification :', max_length=100)
    # doj = forms.DateTimeField(label='Date Of Joining :')
    # designation = forms.CharField(label='Designation/Role :', max_length=100)
    # NT_skill = forms.CharField(label='Non-Technical Skills :', widget=forms.Textarea, max_length=500)
    # T_skill = forms.CharField(label='Technical skills :', widget=forms.Textarea, max_length=500)
    # file = forms.FileField(label='Upload your Profile Picture :')

    class Meta:
        model = Employee
        #Employee = (Employee.objects.all().order_by('your_name', 'designation', 'highest_degree'))
        fields = ('your_name', 'dob', 'city', 'country', 'highest_degree', 'doj', 'designation')

        # def save(self, commit=True):
        #     employee = super(Employee, self).save(commit=False)
        #     # do custom stuff
        #     if commit:
        #         employee.save()
        #     return employee
# from twisted.test.process_echoer import data
# from django.db import models
# test model
import datetime
from django.utils import timezone
from time import time
from django.db import models
# from django.core.files.storage import FileSystemStorage
from django.conf import settings
from CRS import settings
from gtk._gtk import widget_set_default_colormap


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # this is added to notify that what is created recently, a filter is used in admin.py so as to differentiate as per the date published for the object 'Question'
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


def __unicode__(self):  # __unicode__ on Python 2
    return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.choice_text


STATUS_CHOICES = enumerate(("solid", "squishy", "liquid"))


class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.flavor


# Comment model

class Comment(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')


    def __unicode__(self):  # __unicode__ on Python 2
        return self.first_name

        # userprofile model


from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __unicode__(self):
        # return u'%s,%s,%s' % self.user.username, self.last_name, self.first_name
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'

        # -----------------------------------------------------------------------------------------------------
        # employee information form model
        # -----------------------------------------------------------------------------------------------------

# def get_upload_file_name(instance, filename):
#     return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.', '_'), filename)


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    your_name = models.CharField(max_length=100, default=None)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now())
    city = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
    highest_degree = models.CharField(max_length=100, default=None)
    doj = models.DateTimeField(blank=True, null=True, default=timezone.now())
    designation = models.CharField(max_length=100, default=None)
    Profile_Pic = models.ImageField(upload_to="img/documents/", null=True, blank=True)

    # NT_skill = models.TextField(max_length=500, null=True, blank=True, default=None)
    # T_skill = models.CharField(max_length=500, default=None)

    def __unicode__(self):
        # return u'%s,%s,%s' % self.user.username, self.last_name, self.first_name
        return self.your_name

    # def get_thumbnail(self):
    #     thumb = str(self.thumbnail)
    #     if not settings.DEBUG:
    #         thumb = thumb.replace('rEcScorE/', '')
    #
    #     return thumb
# -----------------------------------------------------------------------------------------------------
# testing models forms
# -----------------------------------------------------------------------------------------------------
# from django.db import models

#
# from django.forms import ModelForm
#
# TITLE_CHOICES = (
# ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# )
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#     birth_date = models.DateField(blank=True, null=True)
#
#     def __unicode__(self):  # __unicode__ on Python 2
#         return self.name
#
#
# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     def __unicode__(self):  # __unicode__ on Python 2
#         return self.name
#
# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
#
#
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']
#         help_texts = {
#             'name': _('Some useful help text.'),
#          }

#
from django import forms
#
# class AuthorForm(forms.Form):
# name = forms.CharField(max_length=100)
#     title = forms.CharField(max_length=3,
#                 widget=forms.Select(choices=TITLE_CHOICES))
#     birth_date = forms.DateField(required=False)
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

# from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Choice, Question
from annoying.functions import get_object_or_None

class indexView(TemplateView):
    template_name = 'rEcScorE/index.html'


class flowView(TemplateView):
    template_name = 'rEcScorE/flow.html'


    # def get_queryset(self):
    # """Return the last five published questions."""
    # return Question.objects.order_by('-pub_date')[:5]


# class signupView(generic.ListView):
# template_name = 'rEcScorE/signup.html'
# def get_success_url(self):
# return reverse('rEcScorE/index.html')


#
# class DetailView(generic.DetailView):
# model = Question
# template_name = 'rEcScorE/signup.html'
#
#
# class ResultsView(generic.DetailView):
# model = Question
# template_name = 'rEcScorE/flow.html'
#
#
# def vote(request, question_id):
# model = Question
#     template_name = 'rEcScorE/flow.html'


# -------------------------------------------------------------------------------------------------------------------
# simple login and register using django.contrib.auth
# -------------------------------------------------------------------------------------------------------------------
# from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib import auth
# from django.core.context_processors import csrf

# usercreation form is prebuild and we are utilising the same
# from django.contrib.auth.forms import UserCreationForm
# from forms import MyRegistrationForm
# from django.contrib.formtools.wizard.views import SessionWizardView
# from django.core.mail import send_mail
#
# from celery.result import AsyncResult
# from celery_test.tasks import do_something_long
# from django.core.urlresolvers import reverse
# from django.utils import simplejson as json
#
# import logging
#
# logr = logging.getLogger(__name__)
#
#
# def login(request):
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('accounts/login.html', c)
#
#
# def auth_view(request):
#
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')
#
#
# def loggedin(request):
#     return render_to_response('accounts/loggedin.html',
#                               {'full_name': request.user.username})
#
#
# def invalid_login(request):
#     return render_to_response('accounts/invalid_login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return render_to_response('accounts/logout.html')
# #
# #
# # def register_user(request):
# #     if request.method == 'POST':
# #         form = MyRegistrationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return HttpResponseRedirect('/accounts/register_success')
# #
# #
# #         else:
# #             form = MyRegistrationForm()
# #     args = {}
# #     args.update(csrf(request))
# #
# #     args['form'] = MyRegistrationForm
# #
# #     return render_to_response('accounts/register.html', args)
#
#
# def register_success(request):
#     return render_to_response('accounts/register_success.html')
#


# -------------------------------------------------------------------------------------------------------------------
# view for try for email verification system
# -------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from .forms import*

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and (user.is_active is True):
        auth.login(request, user)
        userid = user.id
        return HttpResponseRedirect('/userprofile/userinfo/%d'%userid)
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('userprofile/userinfo.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logout.html')


# --------------------------------------------------------------------------------------------------------------------
# registering user
# --------------------------------------------------------------------------------------------------------------------
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            # form attributes saved to data then operation applied on data
            # User.first_name.save()
            data = form.save(commit=False)
            data.save()  # save user to database if form is valid
            data.is_active = False
            data.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt + email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user = User.objects.get(username=username, )

            # Create and save user profile

            new_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()
            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                      [email], fail_silently=False)

            return HttpResponseRedirect('/accounts/register_success/')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('accounts/register.html/', args, context_instance=RequestContext(request))


def register_success(request):
    return render_to_response('accounts/register_success.html')


def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('accounts/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    else:
        user = user_profile.user
        user.is_active = True
        user.save()
        return render_to_response('accounts/confirm.html')

# --------------------------------------------------------------------------------------------------------------------
# Employee user form data view
# ---------------------------------------------------------------------------------------------------------------------


@login_required
def get_empprof(request, userid):
    # print userid
        # if this is a POST request we need to process the form data
    instance = get_object_or_None(Employee, pk = int(userid))
    if request.method == 'POST':


    # create a form instance and populate it with data from the request:
       form = EmpProf(request.POST, instance=instance)

    # check whether it's valid:
       if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/userprofile/myprofile/')
       else:
           print form.errors
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmpProf(instance=instance)

    return render(request, 'userprofile/userinfo.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def myprofile(request):
    user = request.user
    user_profile = Employee.objects.filter(user = request.user)

    return render_to_response('userprofile/myprofile.html', {'user_profile': user_profile})

def editprofile(request):

    return render_to_response('userprofile/userinfo.html')
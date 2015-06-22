# from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Choice, Question


class indexView(TemplateView):
    template_name = 'rEcScorE/index.html'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

class signupView(generic.ListView):
      template_name = 'rEcScorE/signup.html'
      # def get_success_url(self):
      #     return reverse('rEcScorE/index.html')



#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'rEcScorE/signup.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'rEcScorE/flow.html'
#
#
# def vote(request, question_id):
#     model = Question
#     template_name = 'rEcScorE/flow.html'

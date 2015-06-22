from django.db import models
# test model
import datetime
from django.utils import timezone

from django.db import models


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

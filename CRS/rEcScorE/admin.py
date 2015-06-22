from django.contrib import admin

# # Register your models here.
# if we want to display the data on index page then define models here also as given below
from django.contrib import admin

from django.contrib import admin

from .models import Choice, Question, IceCream

# #by changing the place of class below we can decide what to keep first and what to keep next
# class QuestionAdmin(admin.ModelAdmin):
# fields = ['pub_date', 'question_text']


# By below class we can show or hide data as per our needs in admin account
# class QuestionAdmin(admin.ModelAdmin):
# fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]

# this will include option to add choices just below the question in  admin account(also we can have tabular representation by changing StackedInline word to TabularInline)
class ChoiceInline(admin.TabularInline):
       model = Choice


extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(IceCream)
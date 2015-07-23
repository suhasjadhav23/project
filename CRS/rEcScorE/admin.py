from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ----------------------------------------------------------------------------------


class CommentAdmin(admin.ModelAdmin):

    list_display = ['user','body', 'pub_date']

    class Meta:
        model = Comment


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name', 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
        }),
    )




# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
# admin.site.register(IceCream)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Employee)
from django.db import models
from django.contrib import admin

from markdownx.widgets import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }

admin.site.register(MyModel, MyModelAdmin)
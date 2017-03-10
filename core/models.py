from __future__ import unicode_literals

from django.db import models

from markdownx.models import MarkdownxField, MarkdownxFormField

class MyModel(models.Model):
    markdownx_field1 = MarkdownxField()
    markdownx_field2 = MarkdownxField()
    markdownx_field3 = MarkdownxField()

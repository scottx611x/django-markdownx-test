from __future__ import unicode_literals

from django.db import models

from markdownx.models import MarkdownxField

class MarkdownPage(models.Model):
    slug = models.SlugField(unique=True)
    markdownx_field1 = MarkdownxField()
    markdownx_field2 = MarkdownxField(blank=True)
    markdownx_field3 = MarkdownxField(blank=True)

    def __str__(self):
        return self.slug
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create a model of Snippets
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='', blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('-created',)  # order by created. Most recent first

    def __unicode__(self):
        return 'snippet %s created on %s' % (self.title, self.created)

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse('snippets:detail', kwargs={'pk': self.id})
# Lets read serializers.py next

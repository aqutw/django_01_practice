from django.db import models
from django.utils.encoding import force_unicode # http://stackoverflow.com/questions/3798137/djangounicodedecodeerror-and-force-unicode

# see also https://docs.djangoproject.com/en/1.7/ref/models/fields/
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def __unicode__(self):
        #return force_unicode(self.title)
        return u'%s' % self.title # http://mozillazg.com/2013/05/django-__unicode__-bad-unicode-data.html


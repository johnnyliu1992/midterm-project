from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Pinter(models.Model):
    OSFA=models.CharField(max_length=500)
    OSFB=models.CharField(max_length=500)
    def __str__(self):
        return '%s %s' % (self.OSFA, self.OSFB)\
        
@python_2_unicode_compatible
class Panno(models.Model):
    genename=models.CharField(max_length=500)
    genefunc=models.CharField(max_length=500)
    genefunc_disc=models.CharField(max_length=100)
    def __str__(self):
        return '%s %s %s' % (self.genename, self.genefunc, self.genefunc_disc)

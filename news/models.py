from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    source = models.CharField(max_length=250, blank = True, null = True)
    author = models.CharField(max_length=100, blank = True, null = True)
    title = models.CharField(max_length=500, blank = True, null = True)
    description = models.CharField(max_length=700, blank = True, null = True)
    url = models.CharField(max_length=250, blank = True, null = True)
    image = models.CharField(max_length=400, blank = True, null = True)
    datetime = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=5000, blank = True, null = True)
    category = models.CharField(max_length=20, blank = True, null = True)

    def __str__(self):
        return self.title
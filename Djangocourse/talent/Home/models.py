from django.db import models

# Create your models here.
class Index(models.Model):
       employeeid = models.CharField(max_length=10, default="0")
       fullname = models.CharField(max_length=2000, blank=True, default='')
       emailid = models.CharField(max_length=2000, blank=True, default='')
       concern = models.TextField(max_length=2000, blank=True, default='')

       def __str__(self):
              return self.emailid
from django.db import models


#from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)




# Create your models here.

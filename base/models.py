from django.db import models

# Create your models here.
class BioData(models.Model):
    fname = models.CharField(max_length= 50)
    lname = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    age = models.IntegerField()  
    nin = models.CharField(max_length= 10, default=None, null=True, blank=True)
    atm = models.CharField(max_length= 15, default=None, null=True)
    updated_at = models.DateTimeField(auto_now= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.fname + ' ' + self.lname
    
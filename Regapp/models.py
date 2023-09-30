from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    uname = models.CharField(max_length=25)
    email = models.EmailField()
    pass1 = models.CharField(max_length=25)
    def __str__(self):
        return self.uname
    
class pro_tbl(models.Model):
    uname = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.TextField(max_length=25)
    picture = models.FileField(upload_to='Images')
    def __str__(self):
        return self.uname
       
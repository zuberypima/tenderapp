from django.db import models

# Create your models here.

class ClientDetail(models.Model):
    idNo=models.CharField(max_length=255)
    orgName=models.CharField(max_length=255)
    CATEGORY =[
        ('Private','Private'),
        ('Public','Public'),
        ('Government','Government')
    ]
    orgCategory=models.CharField(max_length=255,choices=CATEGORY)
    def __str__(self):
        return self.orgName

class Condition (models.Model):
      condition =models.CharField(max_length=255)
      def __str__(self):
        return self.condition
    

class Requirement(models.Model):
    conditionseted =models.OneToOneField(Condition,on_delete=models.CASCADE)
    requirement =models.CharField(max_length=255)

    def __str__(self):
        return self.requirement
    




class CreateCond(models.Model):
    clientDetails=models.ForeignKey(ClientDetail, null=True,blank=True,on_delete=models.DO_NOTHING)
    condDetails=models.CharField(max_length=255)
    condValue=models.CharField(max_length=255)
    def __str__(self):
        return self.condDetails
    
from django.db import models
from procoficer.models import CreateCond,ClientDetail
# Create your models here.
#CreateCond

class Category(models.Model):
    name =models.CharField(max_length=255, unique= True)

    def __str__(self):
        return self.name

class TenderReg(models.Model):
    tenderid = models.CharField(max_length=255)
    cliendName =models.ForeignKey(ClientDetail,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    clinteId = models.CharField(max_length=255, blank=True, null=True)
    deadLineDate = models.DateField()
    procure_method = models.CharField(max_length=255)
    # STATU_TYPE =[
    #     ('Evaluated','Evaluated'),
    #     ('Bid Submission','Bid Submission'),
    #     ('Awarded','Awarded'),
    #     ('Canceled','Canceled')
    # ]
    # tender_status = models.CharField(max_length=255,choices=STATU_TYPE)
    financial_value = models.CharField(max_length=255)
  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.tenderid

# class TenderCond(models.Model):
#       condName=models.ForeignKey(CreateCond, on_delete=models.DO_NOTHING)
#       condition=models.BooleanField(default=False)
#       def __str__(self):
#         return self.condName 
    

# class TenderRequireiment(models.Model):
#     reqname=models.CharField(max_length=200)    
#     def __str__(self):
#         return self.reqname


# class ReqireList(models.Model):
#     name = models.CharField(max_length=100)
#     # inputs = models.ManyToManyField(TenderRequireiment,)
#     inputs = models.CharField(max_length=2500)
#     # rqired =models.ForeignKey(TenderRequireiment,on_delete=models.CASCADE,related_name='correct')
#     rqired =models.BooleanField(default=False)
#     # Add any additional fields for the input list
#     def __str__(self):
#         return self.name

class ReqiredContent(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class ReqiredInput(models.Model):
    name = models.ForeignKey(ReqiredContent,on_delete=models.CASCADE)
    clentinputs = models.CharField(max_length=250)
    def __str__(self):
        return self.clentinputs

class VendorInput(models.Model):
    name = models.ForeignKey(ReqiredContent,on_delete=models.CASCADE)
    vendorinputs = models.CharField(max_length=250)        
    def __str__(self):
        return self.vendorinputs
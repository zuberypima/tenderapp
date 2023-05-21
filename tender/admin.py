from django.contrib import admin
from .models import TenderReg,ReqiredContent,ReqiredInput,VendorInput
# Register your models here.

admin.site.register(TenderReg)
# admin.site.register(TenderCond)
# admin.site.register(TenderRequireiment)
# admin.site.register(ReqireList)
admin.site.register(ReqiredContent)
admin.site.register(ReqiredInput)
admin.site.register(VendorInput)
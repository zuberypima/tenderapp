from django.contrib import admin
from .models import ClientDetail,CreateCond,Condition,Requirement
# Register your models here.
admin.site.register(ClientDetail)
admin.site.register(CreateCond)
admin.site.register(Condition)
admin.site.register(Requirement)
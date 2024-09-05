from django.contrib import admin
from . models import registration
class Admin(admin.ModelAdmin):
       list_display=('id','NAME','FATHERS_NAME','MOTHERS_NAME','DOB','EMAIL',
                     'CONTACT','PINCOAD','ADDRESS')
admin.site.register(registration,Admin)
 
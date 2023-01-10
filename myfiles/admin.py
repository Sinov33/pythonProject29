from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Tur,AdminTur)

class AdminPort(admin.ModelAdmin):
    list_display = ['id', 'nomi','date','tur','rasm1','vaqt']

admin.site.register(Portfolio,AdminPort)

class AdminServise(admin.ModelAdmin):
    list_display = ['id', 'nomi','vaqt','malumot','rasm1']

admin.site.register(Servise,AdminServise)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ism','vaqt','malumot','rasm1','lavozim']

admin.site.register(Team,AdminTeam)


class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name','gmail','title','textt','date']

admin.site.register(Murojaat,AdminMurojaat)

class AdminGmail(admin.ModelAdmin):
    list_display = ['id','gmailii']

admin.site.register(Gmail,AdminGmail)

class AdminPortgmail(admin.ModelAdmin):
    list_display = ['id','gmaili']

admin.site.register(Portgmail,AdminPortgmail)

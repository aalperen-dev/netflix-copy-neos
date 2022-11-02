from django.contrib import admin

# Register your models here.

from .models import * 

class ProfilAdmin(admin.ModelAdmin):
    list_display= ('isim','user','slug')
    list_display_links=('isim',)
    search_fields = ('isim',)# bu alanda en sona virgül eklenmesi şart
    lit_filter =('user',)# bu alanda en sona virgül eklenmesi şart
    # list_editable =('user',)
    readonly_fields=('slug','id')

admin.site.register(Profil,ProfilAdmin)
admin.site.register(Hesap)

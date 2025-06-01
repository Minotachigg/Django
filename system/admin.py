from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Crimelist, Complainlist, Contact, User

admin.site.register(User, UserAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_filter = ('is_staff')
    
class CrimelistAdmin(admin.ModelAdmin):
    list_filter = ('title', 'status', 'date')
    list_display = ['title', 'status']

admin.site.register(Crimelist, CrimelistAdmin)


class ComplainlistAdmin(admin.ModelAdmin):
    list_filter = ('status', 'date')
    list_display = ['title', 'status']

admin.site.register(Complainlist, ComplainlistAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_filter = ('subject', 'date')
    list_display = ['subject', 'date']

admin.site.register(Contact, ContactAdmin)
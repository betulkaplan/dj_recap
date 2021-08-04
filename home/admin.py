from django.contrib import admin
from .models import Contact, Teacher

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'speciality')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Teacher, TeacherAdmin)

# Register your models here.

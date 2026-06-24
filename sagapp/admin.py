from django.contrib import admin

from sagapp.models import Event, Admission, Classes, Eventpicker
# Register your models here
admin.site.register(Classes)
admin.site.register(Eventpicker)


# @admin.register(Admission)
# class AdmissionAdmin(admin.ModelAdmin):
#     list_display = ('fname_of_student', 'mname_of_student',
#                     'lname_of_student', 'class_of_interest', 'parents_name', 'parents_phone', 'parents_email')
#     ordering = ('class_of_interest', 'fname_of_student',)
#     search_fields = ['class_of_interest', 'fname_of_student']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title_of_event', 'time_of_event',
                    'date_of_event', 'date_of_event',)
    ordering = ('title_of_event', 'date_of_event',)
    search_fields = ['date_of_event', 'title_of_event']

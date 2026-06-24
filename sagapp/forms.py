from cProfile import label
from datetime import date, datetime
from .widget import DatePickerInput, TimePickerInput
from django import forms
from sagapp.models import Contact, Event, Admission, Eventpicker


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'enquiry_reason')
        labels = {'name': 'Name', 'email': 'Email Address',
                  'phone': 'Phone Number', 'enquiry_reason': 'Reason for Enquiry', 'sent_on': 'Recieved On'}

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


class EventsForm(forms.ModelForm):

    class Meta:
        model = Event
        widgets = {
            'date_of_event': forms.TextInput({'placeholder': 'mm/dd/yyyy'}),
            'time_of_event': forms.TextInput({'placeholder': 'hh:mm'}),
            'date_of_event': DatePickerInput(),
            'time_of_event': TimePickerInput(),

        }
        fields = ('date_of_event', 'time_of_event',
                  'title_of_event', 'event_content', 'event_photo')
        labels = {'date_of_event': 'Event Date',
                  'time_of_event': 'Time(hh:mm)',
                  'title_of_event': 'Title Of Event',
                  'event_content': 'Event Content',
                  'event_photo': 'Event Photo'}

    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)
        self.fields['date_of_event'].widget.attrs.update(
            {'type': 'date'})
        self.fields['time_of_event'].widget.attrs.update(
            {'type': 'time'})


class EventPickerForm(forms.ModelForm):
    class Meta:
        model = Eventpicker
        fields = ('picker', 'picker_eid')
        labels = {'picker': 'Event Picker Title', 'picker_eid': 'Event ID'}

    def __init__(self, *args, **kwargs):
        super(EventPickerForm, self).__init__(*args, **kwargs)


class AdmissionForm(forms.ModelForm):

    class Meta:
        model = Admission
        widgets = {
            'dob': forms.TextInput({'placeholder': 'dd/mm/yyyy'}),
            'dob': DatePickerInput()
        }
        exclude = ['date_created']
        fields = ('first_name', 'middle_name',
                  'last_name', 'gender',  'date_of_birth', 'clas_of_admission', 'parent_name', 'parent_phone_number', 'parent_email', 'address',)
        labels = {'first_name': 'First Name', 'middle_name': 'Middle Name',
                  'last_name': 'Surname', 'gender': 'Gender', 'date_of_birth': 'Date Of Birth', 'clas_of_admission': 'Class For Admission', 'parent_name': 'Fullname Of Parent',
                   'parent_phone_number': 'Phone Number of Parent',
                  'parent_email': "Parent's Email", 'address': 'Address'}

    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': "Student's First Name"})
        self.fields['middle_name'].widget.attrs.update({'placeholder': "Student's Middle Name"})
        self.fields['last_name'].widget.attrs.update({'placeholder': "Student's Last Name"})
        self.fields['gender'].widget.attrs.update({'type': 'select', 'id': 'selectinput'})
        self.fields['date_of_birth'].widget.attrs.update({'placeholder': "dd/mm/yyyy", 'type': 'date', 'id': 'dobselect'})
        self.fields['clas_of_admission'].widget.attrs.update({'placeholder': 'Select Class', 'id': 'selectinput', 'empty_label': 'select class'})
        self.fields['parent_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['parent_phone_number'].widget.attrs.update({'placeholder': "Parent's Phone Number",})
        self.fields['parent_email'].widget.attrs.update({'placeholder': "Parent's Email", 'type':'email'})
        self.fields['address'].widget.attrs.update({'placeholder': "Home Address",})
        

from multiprocessing import context
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from sagapp.forms import ContactForm, EventsForm, AdmissionForm
from sagapp.models import Event, Contact, Admission, Eventpicker
from django.db.models import F
import itertools

# Create your views here.
try:
    showidids = Eventpicker.objects.filter(picker='First')
    for ei in showidids:
        jkt1 = ei.picker_eid

    showidids = Eventpicker.objects.filter(picker='Second')
    for ei in showidids:
        jkt2 = ei.picker_eid

    showidids = Eventpicker.objects.filter(picker='Third')
    for ei in showidids:
        jkt3 = ei.picker_eid

    showidids = Eventpicker.objects.filter(picker='Fourth')
    for ei in showidids:
        jkt4 = ei.picker_eid

    pk1 = jkt1
    pk2 = jkt2
    pk3 = jkt3
    pk4 = jkt4
except Exception:
    pk1 = 1
    pk2 = 2
    pk3 = 3
    pk4 = 4

counter = itertools.count(1)


def home(request):
    selectede1 = Event.objects.filter(pk=pk1)
    selectede2 = Event.objects.filter(pk=pk2)
    selectede3 = Event.objects.filter(pk=pk3)
    selectede4 = Event.objects.filter(pk=pk4)
    return render(request,
                  'sagapp/index.html',
                  {'selectede1': selectede1,
                   'selectede2': selectede2,
                   'selectede3': selectede3,
                   'selectede4': selectede4,
                   })


# def hompage(request):
#     return redirect(reverse('home/'))


def about(request):
    return render(request, 'sagapp/about.html')


@requires_csrf_token
def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://paystack.com/pay/sagesseadmissionform')

    else:
        form = AdmissionForm()

    return render(request, 'sagapp/admission.html', {'form': form})


@requires_csrf_token
@login_required(login_url='/users/login/')
def dashboard(request):
    return render(request, 'sagapp/dashboard.html')


@login_required(login_url='/users/login/')
def view_admissions(request):
    all_admissions = Admission.objects.all()
    context = {'all_admissions': all_admissions}
    return render(request, 'sagapp/view_admissions.html', context)
   # .order_by('-submitted_on')


@requires_csrf_token
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ("Your enquiry has been received and will be addressed accordingly."))
            return HttpResponseRedirect('/contact/')

    else:
        form = ContactForm()

    return render(request, 'sagapp/contact.html', {'form': form})


@login_required(login_url='/users/login/')
def view_contacts(request):
    all_contacts = Contact.objects.all().order_by('-sent_on')
    numc = Contact.objects.all().count()
    return render(request, 'sagapp/view_contacts.html', {'all_contacts': all_contacts, 'numc': numc})


# delete events
@ login_required(login_url='/users/login/')
def delete_events(request, event_id):
    edevents = Event.objects.get(pk=event_id)
    edevents.delete()
    return HttpResponseRedirect('/events/')


# Delete Contacts
@ login_required(login_url='/users/login/')
def delete_contacts(request, contact_id):
    delcontacts = Contact.objects.get(pk=contact_id)
    delcontacts.delete()
    return HttpResponseRedirect('/view_contacts/')


def enquiry_sent(request):
    return render(request, 'sagapp/enquiry_sent.html')


# Show/view all events
@ login_required(login_url='/users/login/')
def events(request):
    all_events = Event.objects.all().order_by('-date_of_event')
    return render(request, 'sagapp/events.html', {'all_events': all_events})


# Edit Events
@requires_csrf_token
@ login_required(login_url='/users/login/')
def edit_events(request, event_id):
    edevents = Event.objects.get(pk=event_id)
    form = EventsForm(instance=edevents)
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=edevents)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/')
        return ('An Error Ocurred')

    context = {'form': form}
    return render(request, 'sagapp/edit_events.html', context)


# Edit Events
@ login_required(login_url='/users/login/')
def delete_events(request, event_id):
    edevents = Event.objects.get(pk=event_id)
    edevents.delete()
    return HttpResponseRedirect('/events/')


# Add events
@requires_csrf_token
@ login_required(login_url='/users/login/')
def add_events(request):
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/')

    else:
        form = EventsForm()

    return render(request, 'sagapp/add_events.html', {'form': form})


def facility(request):
    return render(request, 'sagapp/facility.html')


def dprivacy(request):
    return render(request, 'sagapp/privacy.html')


def teacherlogin(request):
    return HttpResponseRedirect('https://sagesseacademy.schooltry.com/teacher/login')


def parentlogin(request):
    return HttpResponseRedirect('https://sagesseacademy.schooltry.com/parent/login')

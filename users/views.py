# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
# from django.contrib.auth.forms import UserCreationForm
# from sagapp.forms import ContactForm, EventsForm, AdmissionForm
# from sagapp.models import Event, Contact, Admission


@requires_csrf_token
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sagapp:dashboard')
        else:
            messages.error(
                request, ("An error Occured pleasse try again."))
            return render(request, 'users/login.html', {})

    else:
        messages.error(
            request, ("You have logged out."))
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.info(
        request, ("You have logged out"))
    return redirect('users:login')

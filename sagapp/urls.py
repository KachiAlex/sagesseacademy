from django.urls import path
from sagapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'sagapp'

urlpatterns = [
    path('', views.home, name='home'),
    #     path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('view_admissions/', views.view_admissions, name='view_admissions'),
    path('contact/', views.contact_us, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enquiry_sent/', views.enquiry_sent, name='enquiry_sent'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('delete_contacts/<int:contact_id>/',
         views.delete_contacts, name='delete_contacts'),
    path('events/', views.events, name='events'),
    path('add_events/', views.add_events, name='add_events'),
    path('edit_events/<int:event_id>/', views.edit_events, name='edit_events'),
    path('delete_events/<int:event_id>/',
         views.delete_events, name='delete_events'),
    path('facility/', views.facility, name='facility'),
    path('privacy/', views.dprivacy, name='privacy'),
    path('teacherlogin/', views.teacherlogin, name='teacherlogin'),
    path('parentlogin/', views.parentlogin, name='parentlogin'),
]

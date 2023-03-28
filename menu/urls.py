from django.urls import path

from .views import rdirect

urlpatterns = [
    path('home/', rdirect, {'name': 'Home'}, name='home'),
    path('news/', rdirect, {'name': 'News'}, name='news'),
    path('about/', rdirect, {'name': 'About'}, name='about'),
    path('about/contacts', rdirect, {'name': 'Contacts'}, name='contacts'),
    path('about/contacts/careers', rdirect, {'name': 'Careers'}, name='careers'),
    path('about/contacts/media', rdirect, {'name': 'Media'}, name='media'),
    path('events', rdirect, {'name': 'Events'}, name='events'),
    path('events/webinars', rdirect, {'name': 'Webinars'}, name='webinars'),
]

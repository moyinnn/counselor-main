from django.urls import path
from .views import (
    HomePageView, dashboard, create_article, all_articles, delete_article, edit_article, all_videos, all_appointments, booked_appointments, create_appointment, schedule_appointment, edit_appointment, delete_appointment
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('articles', all_articles, name='articles'),
    path('articles/create', create_article, name='create_article'),
    path('articles/edit/<slug:slug>', edit_article, name='edit_article'),
    path('articles/delete/<slug:slug>', delete_article, name='delete_article'),
    path('appointments', all_appointments, name='appointments'),
    path('booked_appointments', booked_appointments, name='booked_appointments'),
    path('appointment/create', create_appointment, name='create_appointment'),
    path('appointment/edit/<slug:slug>', edit_appointment, name='edit_appointment'),
    path('appointment/schedule/<slug:slug>', schedule_appointment, name='schedule_appointment'),
    path('appointment/delete/<slug:slug>', delete_appointment, name='delete_appointment'),
    path('videos', all_videos, name='videos'),
]

from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.note,name='notes'),
    path('notes/', TemplateView.as_view(template_name="note.html"),name='notes'),
    path("", views.addNote,name='notes'),
]
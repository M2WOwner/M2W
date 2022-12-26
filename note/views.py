from .models import Note
from django.shortcuts import render
from .models import Note
from django.contrib import messages
# /notes -> index 
# Uniform Resource Locator (Adress)


def note(request):
    notes = Note.objects.all()
    return render(request,'note.html',
    {'notes':notes})


def addNote(request):
    Note.objects.all()
    if request.method == "POST":
        Title = request.POST.get('Title')
        Description = request.POST.get('Description')
        Image = request.POST.get('Image')
        obj = Note(Title=Title,Description=Description,Image=Image)
        obj.save()
        # messages.add_message(request, messages.INFO, 'Hello world.')
        messages.success(request, obj)
    return render(request,'note.html')
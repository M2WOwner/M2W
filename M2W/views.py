from django.http import HttpResponse
from django.shortcuts import render
from note.models import Note



def base(request):
    return render(request,'base.html')


def home(request):
    return render(request,'registration/home.html')


def note(request):
    notes = Note.objects.all()
    return render(request,'note.html',
    {'notes':notes})


# def addNote(request):
#     Note.objects.all()
#     if request.method == "POST":
#         Title = request.POST.get('Title')
#         Description = request.POST.get('Description')
#         Image = request.POST.get('Image')
#         obj = Note(Title=Title,Description=Description,Image=Image)
#         obj.save()
#     return render(request,'note.html')

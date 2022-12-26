from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'Image')


admin.site.register(Note, NoteAdmin)




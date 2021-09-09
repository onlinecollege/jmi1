from django.contrib import admin

from .models import Note, Paper, Message

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "date", "your_name")

# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(Paper)
admin.site.register(Message)

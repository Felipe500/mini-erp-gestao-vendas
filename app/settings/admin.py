from django.contrib import admin
from .models import MachineCard


@admin.register(MachineCard)
class ReportCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'deb', 'cre1', 'cre2']


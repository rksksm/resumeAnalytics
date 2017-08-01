# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import JD

from django.contrib import admin


# Register your models here.

def deactivate(self, request, queryset):
    queryset.update(isActive='False')


def activate(self, request, queryset):
    queryset.update(isActive='True')


deactivate.short_description = "Deactivate Job Description"
activate.short_description = "Activate Job Description"


class JDAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'description', 'isActive']
    actions = [deactivate, activate]


admin.site.register(JD, JDAdmin)

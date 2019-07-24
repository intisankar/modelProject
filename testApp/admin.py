# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testApp.models import Employee,UserProfileInfo
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    # the order of the detail page in admin model page
    list_display = ['eno','ename','eaddr','esal']
    # for search field in admin models
    search_fields = ['ename','eno']
    # list filter
    list_filter = ['esal','ename']
    # list views
    list_display = ['ename','esal',]
    # create from the list view
    list_editable = ['esal',]

admin.site.register(Employee,EmployeeAdmin) # EmployeeAdmin for reordering the fields

admin.site.register(UserProfileInfo)

from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Subject)
admin.site.register(models.Subject_refer)
admin.site.register(models.Instructor)
admin.site.register(models.menu_subject)
admin.site.register(models.department)
admin.site.register(models.criterion)
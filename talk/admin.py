from django.contrib import admin
from .models import TalkModel
from . import models
# Register your models here.

admin.site.register(TalkModel)


@admin.register(models.TalkType)
class TalkType(admin.ModelAdmin):
    list_display  = models.TalkType._admin_list_display

@admin.register(models.Alubum)
class Alubum(admin.ModelAdmin):
    list_display = models.Alubum._admin_list_display
    
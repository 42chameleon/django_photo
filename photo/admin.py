from django.contrib import admin
from photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

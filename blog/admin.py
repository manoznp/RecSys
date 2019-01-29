from django.contrib import admin
from blog.models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'action']


admin.site.register(Destination, DestinationAdmin)


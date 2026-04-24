from django.contrib import admin
from .models import Society

# Register your models here.

class SocietyAdmin(admin.ModelAdmin):
    list_display = ["name", "location",]
    list_filter = ["name"]
    
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ("title", "date_posted",)

# admin.site.register(Society)

admin.site.register(Society, SocietyAdmin)


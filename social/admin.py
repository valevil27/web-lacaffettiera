from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name","key")
    def get_readonly_fields(self, request, obj):
        if request.user.groups.filter(name="Staff").exists():  # type: ignore
            return ("key", "name")
        else:
            return ("created", "updated")


admin.site.register(Link, LinkAdmin)
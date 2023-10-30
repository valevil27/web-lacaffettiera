from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', "post_categories")
    list_filter = ("categories__name", )
    ordering = ('author', '-published')
    readonly_fields = ("created", "updated")
    search_fields = ("title","author__username", "categories__name")
    date_hierarchy = "published"
    
    def post_categories(self, obj: Post):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description = "Categorías"

admin.site.register(Post, PostAdmin)
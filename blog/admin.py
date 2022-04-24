from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'datetime_modified', )
    ordering = ('-status', )


# admin.site.register(BlogPost, PostAdmin)



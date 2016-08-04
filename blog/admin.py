from django.contrib import admin

from .models import Post


class PostAdmin(admin.AdminSite):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
admin.site.register(Post, PostAdmin)

# admin.site.register(Post)

from django.contrib import admin
from .models import Post, Product, Category, Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_dislay = ('post', 'text', 'created_at')
    search_field = ('post__title', 'text')



admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
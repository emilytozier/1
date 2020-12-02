from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Author
from .models import Comments

class PostInstanceInline(admin.TabularInline):
    model=Comments
    extra=2
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    list_display_links = ['timestamp','updated']
    list_filter= ['timestamp','updated']
    search_fields = ['title','content']
    inlines=[PostInstanceInline]
    #fields=('title')
    exclude=('post_likes',)
    class Meta:
        model=Post

class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','second_name','email']
    list_display_links = ['first_name','second_name']
    search_fields = ['first_name','second_name']
    class Meta:
        model=Author

class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['comment_text','comment_article']
    list_display_links = ['comment_text','comment_article']
    search_fields = ['comment_text','comment_article']
    list_filter = ['timepublish']
    class Meta:
        model=Comments

admin.site.register(Post, PostModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Comments, CommentsModelAdmin)
from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display =('title','slug','author','publish','created', 'status')
	search_fields =('title','body',)
	prepopulated_fields = {'slug': ('title',)}
	list_display_links =('title','author','status')
	raw_id_fields =('author',)
	date_hierarchy ='publish'
	ordering =('status','publish')
	list_filter =('title','status')


admin.site.register(Post, PostAdmin)
from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import Post

# Register your models here.
@admin.register(Post) 
# admin.site.register(Post) 
 
# admin.site.register() and @admin.register() performs same thing. they register an app in the django admin


#customizing the order of the django admin site
class PostAdmin(admin.ModelAdmin):
  list_display = ['title','slug','author','publish','status']
  list_filter = ['status','created','publish','author']
  search_fields = ['title','body']
  prepopulated_fields = {'slug':('title',)}
  raw_id_fields = ['author']
  date_hierarchy = 'publish'
  ordering = ['status','publish']

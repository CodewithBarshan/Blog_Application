from django.contrib import admin
from .models import Category,Post

# Register your models here.
#For configurartion of Category Admin

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','description','urls','datetime','image_tag')
    search_fields=('title',) # to search in admin panel with category title name


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50 #pagnation #each page will contain 5 posts only 

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
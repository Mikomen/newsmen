from django.contrib import admin
from main.models import Category, Post, CommentItem, About, Contact, GetInTouch
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentItemAdmin(admin.ModelAdmin):
    pass

class AboutAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class GetInTouchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CommentItem, CommentItemAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(GetInTouch,GetInTouchAdmin)
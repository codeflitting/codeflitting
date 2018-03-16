from django.contrib import admin
from codeflitting.quote.models import Wisdom, Joke, Tag, Navbar, Author


class WisdomAdmin(admin.ModelAdmin):
    list_display = ['author', 'english', 'chinese', 'created_time', 'last_modified_time']

    date_hierarchy = 'created_time'
    list_filter = ['created_time']
    # search_fields = ['author']
    filter_horizontal = ('tags',)
    ordering = ['author']

    # def get_fields(self, request, obj=None):
    # Admin新建Ariticle 需要显示的可编辑的字段
    # return [['author', 'views', 'likes'], ['english', 'chinese'], 'tags']


class JokeAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_time', 'last_modified_time']
    ordering = ['last_modified_time']


class NavbarAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'href', 'order']
    list_editable = ['href', 'order']


admin.site.register(Wisdom, WisdomAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Joke, JokeAdmin)
admin.site.register(Tag)
admin.site.register(Author)

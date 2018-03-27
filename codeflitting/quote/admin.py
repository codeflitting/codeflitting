from django.contrib import admin
from codeflitting.quote.models import Wisdom, Tag, Navbar, Author, Topic


class WisdomAdmin(admin.ModelAdmin):
    list_display = ['author', 'Topic', 'english', 'chinese', 'created_time', 'last_modified_time']

    date_hierarchy = 'created_time'
    list_filter = ['created_time']
    # search_fields = ['author']
    filter_horizontal = ('tags',)
    ordering = ['author']

    # def get_fields(self, request, obj=None):
    # Admin新建Ariticle 需要显示的可编辑的字段
    # return [['author', 'views', 'likes'], ['english', 'chinese'], 'tags']


class NavbarAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'href', 'order']
    list_editable = ['href', 'order']


admin.site.register(Wisdom, WisdomAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Topic)

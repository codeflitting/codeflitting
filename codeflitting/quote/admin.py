from django.contrib import admin
from codeflitting.quote.models import Wisdom, Joke, Tag, Navbar, Author


class WisdomAdmin(admin.ModelAdmin):
    list_display = ['author', 'english', 'chinese', 'created_time', 'last_modified_time']
    ordering = ['author']


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

from django.contrib import admin
from codeflitting.quote.models import Wisdom, Joke, WisdomTag


class WisdomAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_time', 'last_modified_time']
    ordering = ['author']


class JokeAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_time', 'last_modified_time']
    ordering = ['last_modified_time']


admin.site.register(Wisdom, WisdomAdmin)
admin.site.register(WisdomTag)
admin.site.register(Joke, JokeAdmin)

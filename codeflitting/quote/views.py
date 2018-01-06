from django.shortcuts import render
from django.views.generic import ListView, DetailView
from codeflitting.quote.models import Wisdom, WisdomTag, Joke, Navbar


class WisdomListView(ListView):
    template_name = 'quote/index.html'
    context_object_name = "wisdom_list"

    def get_queryset(self):
        if 'tag_id' in self.kwargs:
            wisdom_list = Wisdom.objects.filter(tags__in=[self.kwargs.get('tag_id')])
        elif 'author_id' in self.kwargs:
            wisdom_list = Wisdom.objects.filter(author=self.kwargs.get('author_id'))
        else:
            wisdom_list = Wisdom.objects.all()

        return wisdom_list

    def get_context_data(self, **kwargs):
        kwargs['navbar'] = Navbar.objects.order_by('order')
        return super(WisdomListView, self).get_context_data(**kwargs)

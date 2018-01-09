from django.views.generic import ListView, DetailView
from codeflitting.quote.models import Wisdom, Tag, Joke, Navbar, Author


class BaseListView(ListView):
    template_name = 'quote/index.html'

    def get_context_data(self, **kwargs):
        kwargs['navbar'] = Navbar.objects.order_by('order')
        kwargs['site_name'] = 'quotes'
        kwargs['site_url'] = 'quote-index'
        return super(BaseListView, self).get_context_data(**kwargs)


class WisdomListView(BaseListView):
    template_name = 'quote/index.html'
    context_object_name = 'wisdom_list'
    paginate_by = 15

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


class AuthorListView(BaseListView):
    template_name = 'quote/index.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        author_list = {}
        for author in Author.objects.all():
            key = author.name[0]
            if key in author_list:
                author_list[key] = author_list[key] + [author]
            else:
                author_list[key] = [author]
        return author_list


class TagListView(BaseListView):
    template_name = 'quote/index.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        tag_list = {}
        for tag in Tag.objects.all():
            key = tag.name[0]
            if key in tag_list:
                tag_list[key] = tag_list[key] + [tag]
            else:
                tag_list[key] = [tag]
        return tag_list

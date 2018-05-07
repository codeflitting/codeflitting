from django.views.generic import ListView, DetailView
from codeflitting.quote.models import Wisdom, Tag, Navbar, Author, Topic
from django.db.models import Q


class BaseListView(ListView):
    template_name = 'quote/index.html'

    def get_context_data(self, **kwargs):
        kwargs['navbar'] = Navbar.objects.order_by('order')
        kwargs['site_name'] = 'quotes'
        kwargs['site_url'] = 'quote-index'
        kwargs['search'] = 'Search...'
        query = self.request.GET.get('q', None)
        if query:
            kwargs['search'] = query
        return super(BaseListView, self).get_context_data(**kwargs)


class WisdomListView(BaseListView):
    context_object_name = 'wisdom_list'
    paginate_by = 20

    def get_queryset(self):
        if 'tag_id' in self.kwargs:
            wisdom_list = Wisdom.objects.filter(tags__in=[self.kwargs.get('tag_id')])
        elif 'author_id' in self.kwargs:
            wisdom_list = Wisdom.objects.filter(author=self.kwargs.get('author_id'))
        elif 'topic_id' in self.kwargs:
            wisdom_list = Wisdom.objects.filter(topic=self.kwargs.get('topic_id'))
        else:
            wisdom_list = Wisdom.objects.all()

        query = self.request.GET.get('q', None)
        if query:
            wisdom_list = wisdom_list.filter(Q(english__contains=query) | Q(chinese__contains=query))
        return wisdom_list


class WisdomDetailView(DetailView):
    model = Wisdom
    template_name = "quote/detail.html"
    context_object_name = "wisdom"
    pk_url_kwarg = 'wisdom_id'

    def get_object(self, queryset=None):
        wisdom = super(WisdomDetailView, self).get_object()
        wisdom.created_time = wisdom.created_time.strftime('%Y-%m-%d')
        return wisdom

    def get_context_data(self, **kwargs):
        kwargs['site_name'] = 'quotes'
        kwargs['site_url'] = 'quote-index'

        return super(WisdomDetailView, self).get_context_data(**kwargs)


class AuthorListView(BaseListView):
    template_name = 'quote/index.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        author_list = {}
        authors = Author.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            authors = authors.filter(name__contains=query)
        for author in authors:
            key = author.name[0]
            if key in author_list:
                author_list[key] = author_list[key] + [author]
            else:
                author_list[key] = [author]
        return author_list

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Authors - '
        kwargs['keydords'] = ','.join([author.name for author in Author.objects.all()])
        kwargs['descrip'] = '-author'
        return super(AuthorListView, self).get_context_data(**kwargs)


class TopicListView(BaseListView):
    template_name = 'quote/index.html'
    model = Topic
    context_object_name = 'topic_list'

    def get_queryset(self):
        topic_list = Topic.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            topic_list = topic_list.filter(name__contains=query)
        return topic_list

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Tags - '
        kwargs['keydords'] = ','.join([tag.name for tag in Tag.objects.all()])
        kwargs['descrip'] = '-tags'
        return super(TopicListView, self).get_context_data(**kwargs)


class TagListView(BaseListView):
    template_name = 'quote/index.html'
    model = Tag
    context_object_name = 'tag_list'

    def get_queryset(self):
        tag_list = Tag.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            tag_list = tag_list.filter(name__contains=query)
        return tag_list

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Tags - '
        kwargs['keydords'] = ','.join([tag.name for tag in Tag.objects.all()])
        kwargs['descrip'] = '-tags'
        return super(TagListView, self).get_context_data(**kwargs)

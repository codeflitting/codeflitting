from django.conf.urls import url
from codeflitting.quote.views import WisdomListView, AuthorListView, TagListView, TopicListView, WisdomDetailView

urlpatterns = [
    url(r'^$', WisdomListView.as_view(), name="quote-index"),
    url(r'^(?P<wisdom_id>\d+)$', WisdomDetailView.as_view(), name='quote-wisdom'),
    url(r'^tag/(?P<tag_id>\d+)$', WisdomListView.as_view(), name='quote-tag'),
    url(r'^tags', TagListView.as_view(), name='quote-tags'),
    url(r'^topic/(?P<topic_id>\d+)$', WisdomListView.as_view(), name='quote-topic'),
    url(r'^topics', TopicListView.as_view(), name='quote-topics'),
    url(r'^author/(?P<author_id>\d+)$', WisdomListView.as_view(), name='quote-author'),
    url(r'^authors', AuthorListView.as_view(), name='quote-authors'),
]

from django.conf.urls import url
from codeflitting.quote.views import WisdomListView, AuthorListView, TagListView

urlpatterns = [
    url(r'^$', WisdomListView.as_view(), name="quote-index"),
    url(r'^tag/(?P<tag_id>\d+)$', WisdomListView.as_view(), name='quote-tag'),
    url(r'^tags', TagListView.as_view(), name='quote-tags'),
    url(r'^author/(?P<author_id>\d+)$', WisdomListView.as_view(), name='quote-author'),
    url(r'^authors', AuthorListView.as_view(), name='quote-authors'),
]

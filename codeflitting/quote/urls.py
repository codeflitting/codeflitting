from django.conf.urls import url
from codeflitting.quote.views import WisdomListView

urlpatterns = [
    url(r'^$', WisdomListView.as_view(), name="quote-index"),
    url(r'^tag/(?P<tag_id>\d+)$', WisdomListView.as_view(), name='quote-tag'),
    url(r'^author/(?P<author_id>\d+)$', WisdomListView.as_view(), name='quote-author'),
]

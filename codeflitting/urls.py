"""codeflitting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from codeflitting.quote.models import Author as QuoteAuthor
from codeflitting.quote.models import Tag as QuoteTag
from codeflitting.quote.models import Wisdom as QuoteWisdom
from codeflitting.quote.models import Topic as QuoteTopic

sitemaps = {
    'quote:wisdom': GenericSitemap({'queryset': QuoteWisdom.objects.all(), 'date_field': 'created_time'}, priority=0.9),
    'quote:topic': GenericSitemap({'queryset': QuoteTopic.objects.all(), 'date_field': 'created_time'}, priority=0.7),
    'quote:author': GenericSitemap({'queryset': QuoteAuthor.objects.all(), 'date_field': 'created_time'}, priority=0.5),
    'quote:tag': GenericSitemap({'queryset': QuoteTag.objects.all(), 'date_field': 'created_time'}, priority=0.3),
    # 如果还要加其它的可以模仿上面的
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quote/', include('codeflitting.quote.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('codeflitting.core.urls')),
]

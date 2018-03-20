from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name="core-index"),
    url(r'^test', TemplateView.as_view(template_name='test/test.html'), name="core-test"),
]

from django.conf.urls.defaults import *
from xtinebooks.bookapp.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)
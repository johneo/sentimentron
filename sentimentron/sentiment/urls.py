from django.conf.urls import patterns, url

urlpatterns = patterns('sentimentron.sentiment.views',
    url(r'^$', 'index'),
)

<<<<<<< HEAD
from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # syntax: url(regex,view,kwargs,name)
    # When Django finds a regex math, it calss the specified view func
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/picture
    url(r'pictureSlideshow.html/$', views.PictureView.as_view(), name = 'picture'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # for display frame in model
    url(r'^frameFromModel/$', views.frameFromModel, name='frameFromModel'),

    

=======
from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # syntax: url(regex,view,kwargs,name)
    # When Django finds a regex math, it calss the specified view func
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/picture
    url(r'pictureSlideshow.html/$', views.PictureView.as_view(), name = 'picture'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # for display frame in model
    url(r'frameFromModel.html/$', views.frameFromModel, name='frameFromModel'),
>>>>>>> origin/master
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
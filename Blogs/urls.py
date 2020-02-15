from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_blog/', views.new_blog, name='new_blog'),
   # url(r'^new_topic/$', views.new_topic, name='new_topic'),
]

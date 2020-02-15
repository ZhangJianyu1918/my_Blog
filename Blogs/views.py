from django.shortcuts import render 
from django.http import HttpResponseRedirect 
from .forms import TopicForm, EntryForm
from django.urls import reverse
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'Blogs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'Blogs/topics.html', context)

def new_blog(request):
    """添加新主题"""          
    return render(request, 'Blogs/new_blog.html')


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    Blogs = topic.blog_set.order_by('-date_added')
    context = {'topic':topic, 'Blogs':Blogs}
    return render(request, 'Blogs/topic.html', context)

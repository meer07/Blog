#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Blog
from cms.pagination import pagination
from cms.tag_search import tag_search

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('id')
    page = request.GET.get('page')
    paged_blogs = make_page(blogs,page)
    tag_list = tag_search.tag_list()
    return render_to_response('blog_list.html',
                              {'blogs':paged_blogs, 'tag_list':tag_list},
                              context_instance=RequestContext(request))

def tag_seach(request):
    tag = request.GET.get('tag')
    seached_context = Blog.objects.filter(tag=tag)
    paged_blogs = make_page(seached_context,tag)
    tag_list = tag_search.tag_list()
    return render_to_response('blog_list.html',
                              {'blogs':paged_blogs, 'tag_list':tag_list},
                              context_instance=RequestContext(request))

def make_page(context, key):
    paginator = pagination(context)
    page = paginator.make_pagination(key)

    return page
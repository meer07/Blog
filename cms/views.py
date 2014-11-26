#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Blog
from cms.pagination import pagination

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('id')
    paginator = pagination(blogs)
    page = request.GET.get('page')
    paged_blogs = paginator.make_pagination(page)

    return render_to_response('blog_list.html',{'blogs':paged_blogs},context_instance=RequestContext(request))

def tag_seach(request):
    tag = request.GET.get('get')
    seached_context = Blog.objects.all().order_by(tag)
    paginator = pagination(seached_context)
    paged_blogs = paginator.make_pagination(tag)

    return render_to_response('blog_list.html',{'blogs':paged_blogs},context_instance=RequestContext(request))
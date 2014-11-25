#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('id')
    return render_to_response('blog_list.html',{'blogs':blogs},context_instance=RequestContext(request))

def blog_edit(request,title=None,date=None,tag=None,log_body=None):
    return HttpResponse(u'ブログをつける')

def blog_del(request,blog_id):
    return HttpResponse(u'ブログの削除')
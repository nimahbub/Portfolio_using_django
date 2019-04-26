from django.shortcuts import render,get_object_or_404
from . models import Blog
blogs=Blog.objects.all


def allblogs(request):
    return render(request,'blog/blog.html',{'blogs':blogs})
def detail(request,blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})

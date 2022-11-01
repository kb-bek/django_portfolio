from django.shortcuts import render, get_object_or_404
from .models import *

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs':blogs
    }

    return render(request, template_name='blog.html', context=context)

def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {'blog':blog}
    return render(request, template_name='blog-detail.html', context=context)
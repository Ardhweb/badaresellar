from multiprocessing import context
from django.shortcuts import render,get_object_or_404

# Create your views here.
from blog.models import Post

def blog_page(request):
    post_list = Post.objects.all()
    context= {'post_list':post_list}
    return render(request, 'blog/list.html', context)



def post_detail(request, id=None):
    # post = get_object_or_404(id=id,klass=Post)
    post_obj = Post.objects.get(id=id)
    context= {'post_obj':post_obj}
    return render(request, 'blog/detail.html', context)
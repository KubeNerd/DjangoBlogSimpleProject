from django.shortcuts import render
from .models import Post

# Create your views here.
def teste(request):
    objects = Post.objects.all()
    template_name = 'home.html'
    posts = {
        'posts':objects
    }
    return render(request, template_name, posts)

def post(request, post_id):
    objects = Post.objects.get(pk=post_id)
    post = {'post':objects}
    template_name = 'post.html'
    return render(request, template_name,  post)


#https://www.youtube.com/watch?v=eK2sfDWQUXc
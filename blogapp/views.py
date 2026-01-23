from django.shortcuts import render , get_object_or_404
from . models import Post

# Create your views here.
def home(request):
    all_post = Post.newmanager.all()
    
    return render(request , 'index.html' , {'posts' : all_post})

def aboutus(request):
    return render(request , 'aboutus.html')

def post_single(request, post):
    single_post = get_object_or_404(Post, slug=post)
    return render(request, 'single.html', {
        'post': single_post
    })
     
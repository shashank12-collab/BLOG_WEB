from django.shortcuts import render
from . models import Post

# Create your views here.
def home(request):
    all_post = Post.objects.all()
    
    return render(request , 'index.html' , {'posts' : all_post})

def aboutus(request):
    return render(request , 'aboutus.html')

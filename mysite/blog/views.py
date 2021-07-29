from django.shortcuts import render
from .models import Post
"""
request = o que entra (o que o navegador envia)
response = response (o que nós retornamos para o navegador)
"""
# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(
        request, 
        'blog/post_list.html',
        {'post_list': posts}
    )

from django.shortcuts import get_object_or_404, render
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request, 
        'blog/post_detail.html',
        {'post': post}
    )
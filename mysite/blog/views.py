from django.shortcuts import render
"""
request = o que entra (o que o navegador envia)
response = response (o que nós retornamos para o navegador)
"""
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product criado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    return render(request, 'estoque/criar_produto.html', {'form': form})

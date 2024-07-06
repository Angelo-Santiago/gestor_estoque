from django.shortcuts import redirect, render

from .forms import CategoriaForm, EmbalagemForm, LocalForm, ProdutoForm
from .models import Categoria, Embalagem, Local, Produto


def home(request):
    return render(request, 'menu.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def listar_embalagens(request):
    consulta = request.GET.get('consulta')
    sigla = request.GET.get('sigla')
    locais = Local.objects.all()
    embalagens = Embalagem.objects.all()
    if consulta:
        embalagens = embalagens.filter(nome__icontains=consulta)
    if sigla:
        locais = locais.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagens.html', {'embalagens': embalagens})


def adicionar_embalagem(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagens.html', {'form': form})


def editar_local(request, id):
    local = Local.objects.filter(id=id).first()
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def excluir_local(request, id):
    local = Local.objects.filter(id=id).first()
    if request.method == 'GET':
        local.delete()
        return redirect('listar_locais')


def editar_embalagem(request, id):
    embalagem = Embalagem.objects.filter(id=id).first()
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagem)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm(instance=embalagem)
    return render(request, 'produtos/adicionar_embalagens.html', {'form': form})


def excluir_embalagem(request, id):
    embalagem = Embalagem.objects.filter(id=id).first()
    if request.method == 'GET':
        embalagem.delete()
        return redirect('listar_embalagens')


def listar_categorias(request):
    consulta = request.GET.get('consulta')
    categorias = Categoria.objects.all()
    if consulta:
        categorias = categorias.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_categorias.html', {'categorias': categorias})


def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/adicionar_categoria.html', {'form': form})


def editar_categoria(request, id):
    categoria = Categoria.objects.filter(id=id).first()
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'produtos/adicionar_categoria.html', {'form': form})


def excluir_categoria(request, id):
    categoria = Categoria.objects.filter(id=id).first()
    if request.method == 'GET':
        categoria.delete()
        return redirect('listar_categorias')


def listar_produtos(request):
    consulta = request.GET.get('consulta')
    produtos = Produto.objects.all()
    categorias = request.GET.get('categoria')
    embalagens = request.GET.get('embalagens')
    estoque_minimo = request.GET.get('estoque_minimo')
    estoque_maximo = request.GET.get('estoque_maximo')
    locais = Local.objects.all()
    if consulta:
        produtos = produtos.filter(nome__icontains=consulta)
    if categorias:
        locais = locais.filter(categorias=categorias)
    if embalagens:
        locais = locais.filter(embalagens=embalagens)
    if estoque_minimo:
        locais = locais.filter(estoque_minimo=estoque_minimo)
    if estoque_maximo:
        locais = locais.filter(estoque_maximo=estoque_maximo)
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})


def adicionar_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produtos.html', {'form': form})


def editar_produto(request, id):
    produto = Produto.objects.filter(id=id).first()
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/adicionar_produtos.html', {'form': form})


def excluir_produto(request, id):
    produto = Produto.objects.filter(id=id).first()
    if request.method == 'GET':
        produto.delete()
        return redirect('listar_produtos')

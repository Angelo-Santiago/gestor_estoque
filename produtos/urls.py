from django.urls import path

from .views import (
    adicionar_categoria,
    adicionar_embalagem,
    adicionar_local,
    adicionar_produtos,
    editar_categoria,
    editar_embalagem,
    editar_local,
    editar_produto,
    excluir_categoria,
    excluir_embalagem,
    excluir_local,
    excluir_produto,
    home,
    listar_categorias,
    listar_embalagens,
    listar_locais,
    listar_produtos,
)

urlpatterns = [
    path('', home, name='home'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produtos, name='adicionar_produtos'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categoria, name='adicionar_categoria'),
    path('locais/<int:id>/editar', editar_local, name='editar_local'),
    path('locais/<int:id>/excluir', excluir_local, name='excluir_local'),
    path('embalagem/<int:id>/editar', editar_embalagem, name='editar_embalagem'),
    path('embalagem/<int:id>/excluir', excluir_embalagem, name='excluir_embalagem'),
    path('categoria/<int:id>/editar', editar_categoria, name='editar_categoria'),
    path('categoria/<int:id>/excluir', excluir_categoria, name='excluir_categoria'),
    path('produtos/<int:id>/editar', editar_produto, name='editar_produto'),
    path('produtos/<int:id>/excluir', excluir_produto, name='excluir_produto')
]

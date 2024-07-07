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
    listar_fornecedores,
    adicionar_fornecedores,
)

urlpatterns = [
    path('', home, name='home'),

    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('locais/<int:id>/editar', editar_local, name='editar_local'),
    path('locais/<int:id>/excluir', excluir_local, name='excluir_local'),

    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produtos, name='adicionar_produtos'),
    path('produtos/<int:id>/editar', editar_produto, name='editar_produto'),
    path('produtos/<int:id>/excluir', excluir_produto, name='excluir_produto'),
   
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),
    path('embalagem/<int:id>/editar', editar_embalagem, name='editar_embalagem'),
    path('embalagem/<int:id>/excluir', excluir_embalagem, name='excluir_embalagem'),

    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', adicionar_fornecedores, name='adicionar_fornecedores'),

    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categoria, name='adicionar_categoria'),
    path('categoria/<int:id>/editar', editar_categoria, name='editar_categoria'),
    path('categoria/<int:id>/excluir', excluir_categoria, name='excluir_categoria'),
 
]

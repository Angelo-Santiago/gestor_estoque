from django import forms

from .models import Categoria, Embalagem, Local, Produto, Fornecedor


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'tipo']


class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem
        fields = ['name', 'sigla']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'nome_fantasia', 'produtos']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'embalagens', 'estoque_minimo', 'estoque_maximo']

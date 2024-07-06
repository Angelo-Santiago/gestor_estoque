from django import forms

from .models import Categoria, Embalagem, Local, Produto


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'tipo']


class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem
        fields = ['name', 'sigla']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'embalagens', 'estoque_minimo', 'estoque_maximo']

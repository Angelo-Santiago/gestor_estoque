from django.db import models

from utils.base_models import BaseModel


class Local(BaseModel):
    TIPO_DE_LOCAL = [('F', 'Fisico'), ('D', 'Digital')]
    nome = models.CharField(
        max_length=50, verbose_name='Nome do local armazenado', unique=True
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_DE_LOCAL,
        verbose_name='Tipo do local movimentação',
    )

    class Meta:
        db_table = 'locais'

    def __str__(self):
        return self.name


class Movimentacao(BaseModel):
    TIPO_MOVIMENTACAO = [
        (1, 'Entrada'),
        (-1, 'Saída'),
    ]
    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='Produto da movimentação',
    )
    fornecedor = models.ForeignKey(
        'produtos.Fornecedor',
        on_delete=models.CASCADE,
        verbose_name='Fornecedor do produto movimentação',
    )
    quantidade = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name='Quantidade movimentada',
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name='Preço do produto na movimentação',
    )
    codigo_fabricante = models.CharField(
        max_length=20,
        verbose_name='Código do fabricante',
    )
    local = models.ForeignKey(
        'produtos.Local',
        on_delete=models.CASCADE,
        verbose_name='Local da movimentação',
    )
    tipo = models.IntegerField(
        choices=TIPO_MOVIMENTACAO,
        verbose_name='Tipo de movimentação',
    )

    class Meta:
        db_table = 'movimentacoes'

    def __str__(self):
        return self.name


class Embalagem(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name='Nome da embalagem',
    )
    sigla = models.CharField(
        max_length=3,
        verbose_name='Sigla da embalagem',
    )

    class Meta:
        db_table = 'embalagens'

    def __str__(self):
        return self.sigla


class Fornecedor(BaseModel):
    razao_social = models.CharField(
        max_length=100, verbose_name='Razão social do fornecedor', unique=True
    )
    nome_fantasia = models.CharField(
        max_length=100,
        verbose_name='Nome fantasia do fornecedor',
    )
    produtos = models.ManyToManyField(
        'produtos.Produto',
        verbose_name='Produtos fornecedor',
    )

    class Meta:
        db_table = 'fornecedores'

    def __str__(self):
        return self.name


class Produto(BaseModel):
    nome = models.CharField(
        max_length=100,
        verbose_name='nome do produto',
    )
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='categoria do produto',
    )
    embalagens = models.ManyToManyField(
        'produtos.Embalagem',
        verbose_name='Embalagens do produto',
    )
    estoque_minimo = models.FloatField(
        verbose_name='Estoque minimo do produto',
    )
    estoque_maximo = models.FloatField(
        verbose_name='Estoque maximo do produto',
    )

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.name


class Categoria(BaseModel):
    name = models.CharField(
        max_length=100, verbose_name='nome da categoria', unique=True
    )

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.name

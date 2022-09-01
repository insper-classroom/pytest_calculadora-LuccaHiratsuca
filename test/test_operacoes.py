import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import numpy as np

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)

@pytest.mark.op_simples
#Teste de subtração
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1, v2)

@pytest.mark.op_simples
#Teste de multiplicação
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1, v2)

@pytest.mark.op_simples
#Teste de divisão
def test_divisao_dois_valores_positivos():
    v1 = 10.0
    v2 = 2.0
    assert 5.0 == divisao(v1, v2)

@pytest.mark.op_simples
#Teste de média de lista de valores
def test_media_lista_valores_positivos():
    v = [1, 2, 3, 4, 5]
    assert 3 == media_lista_valores(v)

@pytest.mark.op_complexas
#Teste soma com valores negativos
def test_soma_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert -12 == soma(v1, v2)

@pytest.mark.op_complexas
#Teste subtração com valores negativos
def test_sub_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 2 == sub(v1, v2)

@pytest.mark.op_complexas
#Teste multiplicação com valores negativos
def test_multiplicacao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 35 == multiplicacao(v1, v2)

@pytest.mark.op_complexas
#Teste divisão com valores negativos
def test_divisao_dois_valores_negativos():
    v1 = -10.0
    v2 = -2.0
    assert 5.0 == divisao(v1, v2)

@pytest.mark.op_complexas
#Teste média de lista de valores com valores negativos
def test_media_lista_valores_negativos():
    v = [-1, -2, -3, -4, -5]
    assert -3 == media_lista_valores(v)

#Teste de divisão por zero deve retornar np.inf
@pytest.mark.op_complexas
def test_divisao_por_zero():
    v1 = 10.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)


#Teste de média de lista de valores com valores nulos, ignorando os nulos
@pytest.mark.op_complexas
def test_media_lista_valores_nulos():
    v = [1, 2, 3, 4, 5,'abc']
    #List Comprehension com lista apenas de tipos numéricos	
    v_numeros = [x for x in v if isinstance(x, (int, float))]

    assert 3 == media_lista_valores(v_numeros)

#Teste de média com lista vazia, se lista vazia retorna 0
@pytest.mark.op_complexas
def test_media_lista_vazia():
    assert 0 == media_lista_valores([])






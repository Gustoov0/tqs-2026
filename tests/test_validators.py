"""Testes unitários dos validadores de CPF e e-mail.

Mantemos a suíte propositalmente pequena: 1 caso válido + 1 caso inválido
para cada validador. O suficiente para o aluno acompanhar o ciclo TDD
sem se afogar em código de teste.

Os capítulos 5 (TDD) e 10 (atividade prática) sugerem novos testes
para cobrir casos de borda — adicione-os à medida que evoluir o projeto.
"""

from src.validators import validar_cpf, validar_email, validar_cnpj, validar_telefone


#testes para CPF
def test_aceita_cpf_valido():
    assert validar_cpf("111.444.777-35") is True

def test_rejeita_cpf_com_digito_verificador_errado():
    assert validar_cpf("111.444.777-30") is False


#testes para Email
def test_aceita_email_valido():
    assert validar_email("aluno@ufopa.edu.br") is True

def test_rejeita_email_sem_arroba():
    assert validar_email("semarroba.com") is False


#testes para o CNPJ
def test_aceita_cnpj_valido():
    assert validar_cnpj("11.222.333/0001-81") is True

def test_aceita_cnpj_apenas_numeros():
    assert validar_cnpj("11222333000181") is True

def test_rejeita_cnpj_com_digito_verificador_errado():
    assert validar_cnpj("11.222.333/0001-80") is False

def test_rejeita_cnpj_tamanho_invalido():
    assert validar_cnpj("11.222.333/0001") is False


#testes para telefone
def test_aceita_telefone_celular_com_ddd():
    assert validar_telefone("(93) 99123-4567") is True

def test_aceita_telefone_apenas_numeros():
    assert validar_telefone("93991234567") is True

def test_rejeita_telefone_poucos_digitos():
    assert validar_telefone("99123") is False
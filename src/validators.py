"""Validadores de CPF e e-mail.

Lógica de negócio pura, sem dependência de framework web.
Pensada para ser exercitada via TDD na disciplina PC010027 (UFOPA).
"""

import re

_REGEX_EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
_REGEX_TELEFONE = re.compile(r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$")

def _calcular_digito_verificador(digitos: str, peso_inicial: int) -> int:
    pesos = range(peso_inicial, 1, -1)
    soma = sum(int(d) * peso for d, peso in zip(digitos, pesos, strict=True))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto


def validar_cpf(cpf: str | None) -> bool:
    if not isinstance(cpf, str):
        return False

    apenas_digitos = re.sub(r"[.\-\s]", "", cpf)

    if len(apenas_digitos) != 11 or not apenas_digitos.isdigit():
        return False

    if len(set(apenas_digitos)) == 1:
        return False

    primeiro = _calcular_digito_verificador(apenas_digitos[:9], peso_inicial=10)
    segundo = _calcular_digito_verificador(apenas_digitos[:10], peso_inicial=11)

    return apenas_digitos[9] == str(primeiro) and apenas_digitos[10] == str(segundo)


def validar_email(email: str | None) -> bool:
    if not isinstance(email, str) or not email:
        return False
    return _REGEX_EMAIL.match(email) is not None


def _calcular_digito_cnpj(digitos: str) -> int:
    if len(digitos) == 12:
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    else:
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
    soma = sum(int(d) * peso for d, peso in zip(digitos, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_cnpj(cnpj: str | None) -> bool:
    if not isinstance(cnpj, str):
        return False

    apenas_digitos = re.sub(r"[./\-\s]", "", cnpj)

    if len(apenas_digitos) != 14 or not apenas_digitos.isdigit():
        return False

    if len(set(apenas_digitos)) == 1:
        return False

    primeiro = _calcular_digito_cnpj(apenas_digitos[:12])
    segundo = _calcular_digito_cnpj(apenas_digitos[:13])

    return apenas_digitos[12] == str(primeiro) and apenas_digitos[13] == str(segundo)


def validar_telefone(telefone: str | None) -> bool:
    if not isinstance(telefone, str) or not telefone:
        return False

    if not _REGEX_TELEFONE.match(telefone):
        return False

    apenas_digitos = re.sub(r"[\(\)\-\s]", "", telefone)
    return len(apenas_digitos) in (10, 11) and apenas_digitos.isdigit()
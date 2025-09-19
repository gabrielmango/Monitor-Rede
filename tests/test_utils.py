"""Testes do módulo utils"""

from app.utils import log_message


def test_log_message() -> None:
    """Testa registro de mensagem"""
    log_message('teste')
    assert True

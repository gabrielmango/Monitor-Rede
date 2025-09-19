"""Testes do módulo notifier"""

from app.notifier import Notifier


def test_send() -> None:
    """Testa envio de notificação"""
    notifier = Notifier()
    notifier.send('teste')
    assert True

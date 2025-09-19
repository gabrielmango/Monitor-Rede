"""Testes do módulo monitor"""

from app.monitor import Monitor


def test_check_host() -> None:
    """Testa verificação de host"""
    monitor = Monitor()
    assert monitor.check_host('localhost', 1) is False

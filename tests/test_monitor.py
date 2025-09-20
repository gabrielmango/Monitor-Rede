"""Testes do módulo monitor"""

import pytest

from app.monitor import Monitor


def test_check_host_sucesso(monkeypatch: pytest.MonkeyPatch) -> None:
    """Testa verificação de host válido"""

    def mock_check_host(host: str, timeout: int) -> bool:
        return True

    monitor = Monitor()
    monkeypatch.setattr(monitor, 'check_host', mock_check_host)

    assert monitor.check_host('google.com', 5) is True


def test_check_host_falha(monkeypatch: pytest.MonkeyPatch) -> None:
    """Testa verificação de host inválido"""

    def mock_check_host(host: str, timeout: int) -> bool:
        return False

    monitor = Monitor()
    monkeypatch.setattr(monitor, 'check_host', mock_check_host)

    assert monitor.check_host('host-invalido', 5) is False

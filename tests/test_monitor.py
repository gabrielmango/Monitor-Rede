"""Testes do módulo monitor"""

import pytest

from app.monitor import Monitor
from app.notifier import Notifier


class DummyNotifier(Notifier):
    """Notificador de teste sem log em arquivo"""

    def __init__(self) -> None:
        self.messages = []

    def send(self, message: str, level: str = 'info') -> None:
        self.messages.append((level, message))


def test_check_host_sucesso(monkeypatch: pytest.MonkeyPatch) -> None:
    """Testa host acessível"""

    monitor = Monitor(['google.com'], DummyNotifier())

    def fake_gethostbyname(_: str) -> str:
        return '127.0.0.1'

    monkeypatch.setattr('socket.gethostbyname', fake_gethostbyname)

    assert monitor.check_host('google.com') is True


def test_check_host_falha(monkeypatch: pytest.MonkeyPatch) -> None:
    """Testa host inacessível"""

    monitor = Monitor(['nohost.local'], DummyNotifier())

    def fake_gethostbyname(_: str) -> None:
        raise OSError('host not found')

    monkeypatch.setattr('socket.gethostbyname', fake_gethostbyname)

    assert monitor.check_host('nohost.local') is False

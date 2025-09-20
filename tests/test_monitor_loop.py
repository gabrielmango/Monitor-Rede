"""Testes do loop contínuo do Monitor"""

import pytest

from app.monitor import Monitor
from app.notifier import Notifier


class DummyNotifier(Notifier):
    """Notificador de teste sem log em arquivo"""

    def __init__(self) -> None:
        self.messages = []

    def send(self, message: str, level: str = 'info') -> None:
        self.messages.append((level, message))


def test_run_forever_runs_once(monkeypatch: pytest.MonkeyPatch) -> None:
    """Testa execução única dentro de run_forever"""

    notifier = DummyNotifier()
    monitor = Monitor(['google.com'], notifier, interval=1)

    # Mockar host como sempre resolvendo
    def fake_gethostbyname(_: str) -> str:
        return '127.0.0.1'

    monkeypatch.setattr('socket.gethostbyname', fake_gethostbyname)

    calls = {'count': 0}

    def fake_sleep(_: int) -> None:
        calls['count'] += 1
        if calls['count'] >= 1:
            raise KeyboardInterrupt()  # simula CTRL+C

    monkeypatch.setattr('time.sleep', fake_sleep)

    with pytest.raises(KeyboardInterrupt):
        monitor.run_forever()

    assert any(
        'Iniciando monitoramento' in msg for _, msg in notifier.messages
    )
    assert any('google.com' in msg for _, msg in notifier.messages)

"""Testes do módulo notifier"""

import logging
from pathlib import Path

from app.notifier import Notifier


def test_notifier_console_and_log(tmp_path: Path) -> None:
    """Testa envio de notificação no console e log em arquivo"""

    log_file = tmp_path / 'monitor.log'
    notifier = Notifier(log_file=str(log_file))

    notifier.send('Mensagem de sucesso', level='success')
    notifier.send('Mensagem de erro', level='error')
    notifier.send('Mensagem de info')

    # Força flush nos handlers do logger correto ("monitor")
    logger = logging.getLogger('monitor')
    for handler in logger.handlers:
        handler.flush()

    # Verifica se o arquivo de log foi criado
    assert log_file.exists()

    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        assert 'SUCESSO - Mensagem de sucesso' in log_content
        assert 'ERRO - Mensagem de erro' in log_content
        assert 'INFO - Mensagem de info' in log_content

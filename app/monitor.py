"""Módulo de monitoramento de rede"""

import socket
from typing import Optional

import requests

from app.config import load_config
from app.notifier import Notifier


class Monitor:
    """Classe de monitoramento"""

    def __init__(
        self, host: Optional[str] = None, timeout: Optional[int] = None
    ) -> None:
        """Inicializa o monitor"""
        config = load_config()
        self.host: str = host or config.get('TARGET_HOST', 'google.com')
        self.timeout: int = timeout or int(config.get('TIMEOUT', 5))
        self.notifier = Notifier()

    def run(self) -> None:
        """Executa o monitoramento"""
        if self.check_host(self.host, self.timeout):
            self.notifier.send(
                f'Conexão com {self.host} bem-sucedida', level='success'
            )
        else:
            self.notifier.send(
                f'Não foi possível conectar a {self.host}', level='error'
            )

    def check_host(self, host: str, timeout: int) -> bool:
        """Verifica conectividade com um host"""
        try:
            socket.setdefaulttimeout(timeout)
            socket.gethostbyname(host)

            response = requests.get(f'http://{host}', timeout=timeout)
            return response.status_code == 200
        except Exception:
            return False

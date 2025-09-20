"""Módulo de monitoramento"""

import socket
import time
from typing import List

from app.notifier import Notifier


class Monitor:
    """Classe de monitoramento de hosts"""

    def __init__(
        self, hosts: List[str], notifier: Notifier, interval: int = 5
    ) -> None:
        """Inicializa o monitor"""
        self.hosts = hosts
        self.notifier = notifier
        self.interval = interval

    def check_host(self, host: str) -> bool:
        """Verifica se o host está acessível"""
        try:
            socket.gethostbyname(host)
            return True
        except socket.error:
            return False

    def run_once(self) -> None:
        """Executa uma verificação única"""
        for host in self.hosts:
            if self.check_host(host):
                self.notifier.send(
                    f'Conexão com {host} bem-sucedida', level='success'
                )
            else:
                self.notifier.send(
                    f'Falha ao conectar com {host}', level='error'
                )

    def run_forever(self) -> None:
        """Executa verificações contínuas"""
        self.notifier.send(
            f'Iniciando monitoramento a cada {self.interval}s...', level='info'
        )
        while True:
            self.run_once()
            time.sleep(self.interval)

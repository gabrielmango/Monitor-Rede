"""Módulo de notificações"""

import logging
from pathlib import Path
from typing import Optional

from rich.console import Console


class Notifier:
    """Classe de notificação"""

    def __init__(self, log_file: Optional[str] = 'logs/monitor.log') -> None:
        """Inicializa o notificador"""
        self.console = Console()

        # Garantir que pasta existe
        log_path = Path(log_file).parent
        log_path.mkdir(parents=True, exist_ok=True)

        # Configurar logger
        self.logger = logging.getLogger('monitor')
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

    def send(self, message: str, level: str = 'info') -> None:
        """Envia uma notificação"""
        if level == 'success':
            self.console.print(f'[bold green][SUCESSO][/bold green] {message}')
            self.logger.info(f'SUCESSO - {message}')
        elif level == 'error':
            self.console.print(f'[bold red][ERRO][/bold red] {message}')
            self.logger.error(f'ERRO - {message}')
        else:
            self.console.print(f'[bold blue][INFO][/bold blue] {message}')
            self.logger.info(f'INFO - {message}')

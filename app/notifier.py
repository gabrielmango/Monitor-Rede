"""Módulo de notificações"""

import logging
import os
from pathlib import Path
from typing import List, Optional

from rich.console import Console


class Notifier:
    """Classe de notificação"""

    def __init__(self, log_file: Optional[str] = 'logs/monitor.log') -> None:
        """Inicializa o notificador"""
        self.console = Console()
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger('monitor')
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(str(log_path), encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)

        abs_path = os.path.abspath(str(log_path))
        file_handler_already_present = False

        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler_file = getattr(handler, 'baseFilename', None)
                if handler_file and os.path.abspath(handler_file) == abs_path:
                    file_handler_already_present = True
                    break

        if not file_handler_already_present:
            self.logger.addHandler(file_handler)

        # Guardar referência aos file handlers para flush
        self._file_handlers: List[logging.FileHandler] = [
            h
            for h in self.logger.handlers
            if isinstance(h, logging.FileHandler)
        ]

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

        # Garantir escrita imediata no arquivo para testes
        for handler in self._file_handlers:
            try:
                handler.flush()
            except Exception:
                # Nunca lançar exceção por falha de flush durante logging
                pass

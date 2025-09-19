"""Módulo de notificações"""

from rich.console import Console


class Notifier:
    """Classe de notificação"""

    def __init__(self) -> None:
        """Inicializa o notificador"""
        self.console = Console()

    def send(self, message: str, level: str = 'info') -> None:
        """Envia uma notificação"""
        if level == 'success':
            self.console.print(f'[bold green][SUCESSO][/bold green] {message}')
        elif level == 'error':
            self.console.print(f'[bold red][ERRO][/bold red] {message}')
        else:
            self.console.print(f'[bold blue][INFO][/bold blue] {message}')

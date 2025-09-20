"""Ponto de entrada do projeto"""

from app.monitor import Monitor
from app.notifier import Notifier


def main() -> None:
    """Executa o monitoramento"""
    notifier = Notifier()
    monitor = Monitor(['google.com', 'github.com'], notifier, interval=10)
    monitor.run_forever()


if __name__ == '__main__':
    main()

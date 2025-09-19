"""Ponto de entrada da aplicação"""

from app.monitor import Monitor


def main() -> None:
    """Executa o monitoramento de rede"""
    monitor = Monitor()
    monitor.run()


if __name__ == '__main__':
    main()

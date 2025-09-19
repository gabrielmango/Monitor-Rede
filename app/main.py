"""Ponto de entrada da aplicação"""

from app.config import load_config
from app.monitor import Monitor


def main() -> None:
    """Executa o monitoramento de rede"""
    config = load_config()
    monitor = Monitor()
    print(config)  # temporário para validar carregamento
    monitor.run()


if __name__ == '__main__':
    main()

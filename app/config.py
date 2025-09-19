"""Módulo de configuração"""

from pathlib import Path
from typing import Dict

from dotenv import dotenv_values


def load_config(env_file: str = '.env') -> Dict[str, str]:
    """Carrega configurações do sistema"""
    env_path = Path(env_file)

    if not env_path.exists():
        raise FileNotFoundError(f'Arquivo {env_file} não encontrado')

    config: Dict[str, str] = dotenv_values(env_path)  # type: ignore
    return config

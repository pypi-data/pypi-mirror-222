
import json
import os
from pathlib import Path
from abc import ABC, abstractmethod

from ..serialization_utils import serialize_to_file

class EthpwnConfigurable(ABC):
    @abstractmethod
    def get_serializable_config(self):
        raise NotImplementedError

    @abstractmethod
    def load_serialized_config(self, config):
        raise NotImplementedError

    @abstractmethod
    def relative_config_path(self) -> Path:
        raise NotImplementedError

    def store_config(self):
        path = pwn_config_root_dir() / self.relative_config_path()
        serialize_to_file(self.get_serializable_config(), path)

def ethpwn_config_root_dir() -> Path:
    dir = os.path.expanduser('~/.config/ethpwn/')
    os.makedirs(dir, exist_ok=True)
    return Path(dir)

def dbg_config_root_dir():
    dir = os.path.expanduser('~/.config/ethpwn/dbg/')
    os.makedirs(dir, exist_ok=True)
    return dir

def get_default_wallet_path() -> Path:
    return ethpwn_config_root_dir() / 'wallets.json'

def get_default_global_config_path() -> Path:
    return ethpwn_config_root_dir() / 'config.json'

def get_logged_deployed_contracts_dir() -> Path:
    d = ethpwn_config_root_dir() / 'deployed_contracts'
    d.mkdir(parents=True, exist_ok=True)
    return d

def get_contract_registry_dir() -> Path:
    d = ethpwn_config_root_dir() / 'contract_registry'
    d.mkdir(parents=True, exist_ok=True)
    return d

def save_config(out_path):
    with open(out_path, 'w') as f:
        json.dump(GLOBAL_CONFIG, f)

def load_config(in_path, clear=True):
    with open(in_path, 'r') as f:
        loaded = json.load(f)
        if clear:
            GLOBAL_CONFIG.clear()
        GLOBAL_CONFIG.update(loaded)

def reload_default_config():
    GLOBAL_CONFIG.clear()
    GLOBAL_CONFIG.update(load_default_config())


def load_default_config():
    from .wallets import load_default_wallets
    wallets = load_default_wallets()
    result = {
        'wallets': wallets,
    }
    if os.path.isfile(get_default_global_config_path()):
        with open(get_default_global_config_path(), 'r') as f:
            result = json.load(f)

    if 'wallets' not in result:
        result['wallets'] = wallets
    if 'dbg' not in result:
        result['dbg'] = {}
    return result

def save_config_as_default_config(config=None):
    from .wallets import save_default_wallets
    if config is None:
        config = GLOBAL_CONFIG
    if 'wallets' in config:
        wallets = config['wallets']
        save_default_wallets(wallets)
        del config['wallets']
    with open(get_default_global_config_path(), 'w') as f:
        json.dump(config, f, indent=2)

def update_config():
    save_config_as_default_config(GLOBAL_CONFIG)


GLOBAL_CONFIG = None
GLOBAL_CONFIG = load_default_config()

from . import wallets
from . import credentials
from .misc import get_default_node_url, get_default_network



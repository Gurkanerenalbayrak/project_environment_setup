from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    hello: str= "world"

def setup_config():
    cs: ConfigStore = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)


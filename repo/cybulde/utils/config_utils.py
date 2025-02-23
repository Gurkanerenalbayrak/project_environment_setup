# why am i creating extra decorator despite hydra configaration. i wanna create a kind of setup before reading and using hydra config.
from typing import Optional,Any
from hydra.types import TaskFunction
from omegaconf import OmegaConf, DictConfig
from cybulde.config_schemas import config_schema
import yaml 
import logging
import logging.config
import hydra

def get_config(config_path: str, config_name: str) -> TaskFunction:
    setup_config()
    setup_logger

    def main_decorator(task_function: TaskFunction) -> Any:
        @hydra.main(config_path=config_path, config_name=config_name, version_base=None)
        def decorated_main(dict_config: Optional[DictConfig] = None) -> Any:
            config = OmegaConf.to_object(dict_config)
            return task_function(config)
        return decorated_main

    return main_decorator


def setup_config() -> None:
    config_schema.setup_config()

def setup_logger() -> None:
    with open("./cybulde/configs/hydra/job_logging/custom.yaml","r") as stream:
        config: any = yaml.load(stream, leader = yaml.FullLoader)
    logging.config.dictConfig(config)



















from comandor.log import log, FORMAT, DATEFMT
from comandor.models import Setting

from pydantic import ValidationError
from typing import List

import yaml
import json
import sys
import os


def loadSetting(file: str = ".comandor") -> Setting:
    if not os.path.exists(file):
        raise Exception(f"Config file not found! {file}")

    setting: Setting

    with open(file, "r") as f:
        try:
            op = json.load(f)

        except json.JSONDecodeError as e:

            with open(file, "r") as f:
                try:
                    op = yaml.safe_load(f)

                except yaml.error.YAMLError as err:
                    log.error("pars conf error", e, err)
                    raise

    try:
        setting = Setting(**op)
    except ValidationError as e:
        log.error(e)
        raise e

    return setting


def newConfig(
        logfile: str, config: str,
        debug: bool, skip: str) -> Setting:

    setting: Setting = loadSetting(config)
    level: int = log.INFO
    handlers: List = []

    if debug or setting.debug:
        level = log.DEBUG

    if logfile or setting.logfile:
        filename = logfile or str(setting.logfile)
        filemode = "a"
        handlers = [
            log.FileHandler(filename, filemode),
            log.StreamHandler(sys.stdout)
        ]

    log.basicConfig(
        level=level,
        format=FORMAT,
        datefmt=DATEFMT,
        handlers=handlers)

    if debug or setting.debug:
        log.debug("run debug mode!")

    if skip != "":
        log.warn(f"remove action with this match: {skip}")
        for ac in setting.actions:
            if ac.action_name.find(skip) != -1:
                setting.actions.remove(ac)

    log.debug("logger configure!")
    log.debug("loaded Setting!")
    return setting


__all__ = [
    "newConfig",
    "Setting",
]

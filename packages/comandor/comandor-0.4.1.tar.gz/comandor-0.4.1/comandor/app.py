from comandor.errors import errorHandel
from comandor.settings import Setting
from comandor.log import log

from tqdm import tqdm

import subprocess as sp


class App:
    def __init__(self, setting: Setting) -> None:
        self.setting: Setting = setting

    @errorHandel
    def Run(self):
        log.debug("Run action from actions list")

        for action in tqdm(self.setting.actions):
            log.info(f"---- Processing {action.action_name} ----")

            command = f"cd {action.path} && " + " && ".join(action.commands)

            log.info(f"run this command: {command}")
            log.info(f"run with timeout: {action.timeout}")

            log.debug("run command")
            outProcess = sp.check_output(
                command,
                shell=True,
                stderr=sp.STDOUT,
                timeout=action.timeout)

            log.debug("print result from Process")
            log.info(outProcess.decode())
            log.info(f"---- Done Process {action.action_name} ----\n")

        log.info("---- Done All Task! ----")


__all__ = [
    "App",
]

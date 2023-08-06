from tqdm.contrib.logging import logging_redirect_tqdm

from comandor.settings import newConfig, Setting
from comandor.args import read_args
from comandor.log import log
from comandor.app import App


def main():
    args = read_args()
    setting: Setting = newConfig(*args)
    app = App(setting)

    log.info(f"start commander -> {setting.name}")

    with logging_redirect_tqdm():
        app.Run()


if __name__ == "__main__":
    main()


__all__ = [
    "main",
]

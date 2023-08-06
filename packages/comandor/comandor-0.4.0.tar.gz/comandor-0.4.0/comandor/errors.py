from comandor.log import log

import subprocess as sp


def errorHandel(func):
    def wrapper(*a, **kw):
        try:
            log.debug("Run runAction Function")
            return func(*a, **kw)

        except sp.CalledProcessError as err:
            log.error(
                f"Status : FAIL Code: {err.returncode}\n"
                f"OutPut:\n {err.output.decode()}")
            raise

        except IndexError as err:
            log.error(err)
            raise

        except sp.TimeoutExpired:
            log.error("Timeout Error!")
            raise

    return wrapper


__all__ = [
    "errorHandel",
]

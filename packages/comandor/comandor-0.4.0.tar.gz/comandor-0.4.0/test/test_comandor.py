from comandor.settings import newConfig
from comandor.app import App

import unittest
import os


class TestCore(unittest.TestCase):

    def test_ymlAction(self):
        path = os.path.abspath("./test/test_comandor.yml")
        App(newConfig(
            "./log.log",
            path,
            True,
            "",
        )).Run()

    def test_Skip(self):
        path = os.path.abspath("./test/test_comandor.json")
        App(newConfig(
            "./log.log",
            path,
            True,
            "test",
        )).Run()


if __name__ == '__main__':
    unittest.main()

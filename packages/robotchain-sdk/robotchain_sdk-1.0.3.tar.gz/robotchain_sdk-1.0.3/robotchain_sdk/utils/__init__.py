import time
import json
from .loging.loging import Loging

class Utils:

    def __init__(self, framework):
        self._framework = framework
        self.log = Loging()
        self.time = time
        self.json = json

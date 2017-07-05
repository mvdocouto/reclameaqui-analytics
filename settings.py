# -*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

HOST = os.environ.get("HOST","0.0.0.0")
PORT = os.environ.get("PORT", 5000)
DEBUG = True
USE_RELOAD = False
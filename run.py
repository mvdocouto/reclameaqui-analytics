#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from settings import HOST, PORT, DEBUG, USE_RELOAD
import urls

if __name__ == '__main__':
	app.use_reloader = USE_RELOAD
	app.debug = DEBUG
	app.run(host=HOST, port=PORT)


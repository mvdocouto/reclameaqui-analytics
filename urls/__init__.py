# -*- coding: utf-8 -*-
from urls.dashboard import dashboard
from app import app

app.register_blueprint(dashboard, url_prefix='')

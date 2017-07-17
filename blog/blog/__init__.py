# -*- coding: utf-8 -*-

import os
import sys
from flask import Flask

from config import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.append(BASE_DIR)
sys.path.extend([os.path.join(BASE_DIR, child)
                 for child in os.listdir(BASE_DIR) if child[0]!="."])

app = Flask(__name__)
app.config.update(config)


from url_resolve.url import auto_register_url
auto_register_url(app)

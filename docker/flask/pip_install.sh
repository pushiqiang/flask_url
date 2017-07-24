#!/bin/bash

pip install -i https://pypi.doubanio.com/simple  \
        -r /opt/django_deploy/requirements.txt --trusted-host pypi.doubanio.com

# django APP
# do not operate database in APP's docker
# for there would be several apps, sharing one database
#
FROM python:2.7

# 如果在中国，apt 使用镜像
RUN curl -s ifconfig.co/json | python -c "import sys, json; print json.load(sys.stdin)['country']" | grep "China" > /dev/null && \
    curl -s http://mirrors.163.com/.help/sources.list.jessie > /etc/apt/sources.list || true

# 安装开发所需要的一些工具，同时方便在服务器上进行调试
RUN apt-get update;\
    apt-get install -y vim silversearcher-ag gettext postgresql-client graphviz;\
    true

COPY . /opt/django_deploy
WORKDIR /opt/blog

# 先判断是否在中国，如果在中国，使用镜像下载
RUN curl -s ifconfig.co/json | python -c "import sys, json; print json.load(sys.stdin)['country']" | grep "China" > /dev/null && \
    pip install -r /opt/django_deploy/requirements.txt -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com || \
    pip install -r /opt/django_deploy/requirements.txt

RUN mkdir /opt/logging
RUN mkdir /opt/running

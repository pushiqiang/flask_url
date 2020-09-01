FROM python:3.7

# 如果在中国，apt 使用镜像
RUN curl -s http://mirrors.163.com/.help/sources.list.jessie > /etc/apt/sources.list || true

COPY . /opt/docker
WORKDIR /opt/blog

# 先判断是否在中国，如果在中国，使用镜像下载
RUN pip install -r /opt/django_deploy/requirements.txt -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com

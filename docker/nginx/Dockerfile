FROM nginx:1.10.1

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY www.conf /etc/nginx/conf.d/www.conf


COPY custom_404.html /usr/share/nginx/html/custom_404.html

WORKDIR /opt/my_blog

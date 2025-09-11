# CentOS base image
FROM fedora:latest

# Apache (httpd) install karo
RUN echo "Installing httpd"; yum -y install httpd

# apna index.html copy karo /var/www/html/ me
COPY . /var/www/html/

# Container ka port expose karo
EXPOSE 80

# Apache ko foreground mode me run karo
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

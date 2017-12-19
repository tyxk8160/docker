FROM nginx:1.13-alpine
MAINTAINER tramy tramy1234@163.com

COPY flask.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
# this cmd will run on start
#  CMD ["echo","nginx already install"]
CMD ["nginx","-g","daemon off;"]


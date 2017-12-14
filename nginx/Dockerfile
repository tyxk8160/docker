FROM baseos
MAINTAINER tramy tramy1234@163.com
RUN apk add pcre
RUN apk add nginx
RUN mkdir -p /run/nginx
RUN touch /run/nginx/nginx.pid 
EXPOSE 80
# this cmd will run on start
#  CMD ["echo","nginx already install"]
CMD ["nginx","-g","daemon off;"]


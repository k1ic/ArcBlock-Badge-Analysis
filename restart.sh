#!/usr/bin/sh
#killall nginx;/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
ps -ef | grep gunicorn | grep -v grep | awk '{ print "kill -9 " $2}' | sh
gunicorn -c gunicorn_8080.conf server:app --timeout 60

#!/usr/bin/sh
ps -ef | grep gunicorn | grep -v grep | awk '{ print "kill -9 " $2}' | sh
gunicorn -c gunicorn_8080.conf server:app --timeout 60

#!/usr/bin/env bash
# Task 0
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "just testing" | sudo tee /data/web_static/releases/test/index.html
ln -fs  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "46i location /hbnb_static{\nalias /data/web_static/current/;\n}" /etc/nginx/nginx.conf
sudo service nginx restart

#!/usr/bin/env bash
# Task 0
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f -R /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
msg="location /hbnb_static/ {\nalias /data/web_static/current;\n}"
sudo sed -i "40i $msg" /etc/nginx/sites-enabled/default
sudo service nginx restart

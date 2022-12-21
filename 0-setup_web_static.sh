#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static. 

#install nginx
apt-get update
apt-get install -y nginx

# Create a folder
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create a fake html file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

# Create a symbolic link folder
ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

service nginx restart

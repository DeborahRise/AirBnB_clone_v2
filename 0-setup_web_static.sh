#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment

# Install nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
<head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link if it doesn't exist
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
sudo sed -i '/hbnb_static/ {
  s|^.*$|        alias /data/web_static/current/|;
}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

exit 0

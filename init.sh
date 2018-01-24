sudo ﻿ln -sf /home/box/web/etc/gunicorn.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_app
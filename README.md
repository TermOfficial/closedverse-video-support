# closedverse-video-support
so its closedverse, but with video mp4 support and all the features from the other closedverse clones merged into one (thanks arian)

# Requirements
  * Python 3.6.2?
  * Django
  * urllib3?
  * lxml
  * passlib
  * bcrypt
  * mysqlclient if you're using mysql
  * pillow
  * imghdr?
  * markdown

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)
# Setup
1. First, SSH into your server.
2. Update using `sudo apt update && sudo apt upgrade`
3. Install pip if you don't have it already. `sudo apt install pip`
4. Get everything else using pip. `pip3 install Django==3.2.2 urllib3 lxml passlib bcrypt pillow django-markdown-deux django-markdown2 whitenoise django-xff`
5. Clone it. `git clone https://github.com/TermOfficial/closedverse-video-support`
6. Go into the directory. `cd closedverse-video-support`
7. Rename `settings-stripped.py` to `settings.py`
8. Edit the settings. `nano closedverse/settings.py`
9. Fill out everything. Generate a secret key, and paste it in too.
10. Build the database. `python3 manage.py makemigrations closedverse_main` then `python3 manage.py migrate`
11. Build the static files. `python3 manage.py collectstatic`
12. Test the server using `python3 manage.py runserver IP-HERE:80`. Don't forget to put in your public ip in ip here.
13. Create your account using `python3 manage.py createsuperuser` once you've made sure everything is working.
14. Make sure its working, by signing in. Setup your profile.
15. Now lets make this run at boot. `sudo nano /etc/systemd/system/django.service`
16. Paste this into the file.
```
[Unit]
Description=Django Application
After=network.target

[Service]
User=root
WorkingDirectory=/root/Cedar-Django
ExecStart=/usr/bin/python3 manage.py runserver IP-HERE:80

[Install]
WantedBy=multi-user.target
```
17. Put these commands in. `sudo systemctl daemon-reload` then `sudo systemctl enable django` then `sudo systemctl start django`. Make sure it works by running `sudo systemctl status django`
# Copyright
Copyright 2017 Arian Kordi, all rights reserved to their respective owners. (Nintendo, Hatena Co Ltd.)

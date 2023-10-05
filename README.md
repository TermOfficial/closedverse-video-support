
# closedverse-video-support
so its closedverse, but with video mp4 support and all the features from the other closedverse clones merged into one (thanks arian)

# Install/setup
_Updated October 5th, 2023_

Installs like any other Django app. If the tutorial below doesn't help, here are some other ones that accomplish the same thing:
* [Cedar-Django's readme](https://github.com/Mistake35/Cedar-Django/blob/main/README.md)
* [Minihoot's readme](https://github.com/Hoot679/closedverse-video-support/blob/main/README.md)
* [oasisclosed's readme](https://github.com/lunaisnotaboy/oasisclosed/blob/master/readme.md)

If you know what you're doing, you can skip most of the following headlines.
## Install dependencies
You'll need Python, Pip, optionally venv if your operating system needs it, and all of the dependencies.
### Install Python
First things first, make sure Python and Pip are installed on your OS.
* On Ubuntu/Debian, you can run `sudo apt install python3-pip`, and it'll install both.
* For other operating systems, pip _should_ just come from wherever you installed Python.
### Configure venv (YOU CAN SKIP THIS)
I personally don't recommend venv, but if you come across issues normally, you'll need to use it.
* Install venv with `sudo apt install python3-venv`.
* Afterwards, create a virtual env by running: `python3 -m venv closedverse-venv` _(You can use any name you want)_
* After that, if you run `source closedverse-venv/bin/activate`, you will enter that environment.

When you're using venv, **from now on, you will need to remember to run that activate command every time you do anything related to this, whether it's installing packages or running the project. OK?**
### Download this project
Downloading the master.zip and extracting it will work, but it's recommended to use Git.
* Install Git with `sudo apt install git`
* Then run the following:
`git clone https://github.com/TermOfficial/closedverse-video-support`

Now Closedverse should be downloaded to the `closedverse-video-support` folder.
### Install from dependencies.txt
In the `closedverse-video-support` folder, run this:
* `python3 -m pip install -r requirements.txt`

If you install something with pip and see an error saying `error: externally-managed-environment`, **then you'll need to follow the Configure Venv step and try running pip after it's set up.**
* NOTE: some dependencies may give you compiler errors. This is truly a tragedy, but if this does happen, you should install problematic packages through apt, examples: `sudo apt install python3-pil python3-lxml` (UNTESTED WITHIN VENV.)
## Configure Closedverse
If everything is installed and working fine, we can finally move on to configuring Closedverse.
* Open up closedverse/**settings-stripped.py**.
* You'll need to **save it as** closedverse/**settings.py**.
* Fill in SECRET_KEY [using this site, just hit generate.](https://miniwebtool.com/django-secret-key-generator/)
* Put the name of your domain in ALLOWED_HOSTS. _If you forget about this, Django will remind you._

Keep in mind, those are all of the _mandatory_ steps. For everything else, **configure as necessary!**
This is elaborated on in a later section called _Notes about configuration_.
### Migrate/initialize database
After saving settings.py, you can initialize the database by running the following:
* `python3 manage.py makemigrations closedverse_main`
* `python3 manage.py migrate`

Let's make an admin user (_you can choose to do this later_):
* `python3 manage.py createsuperuser`

NOTE: you only have to do the above **for a new database**, or if models.py is updated.

### Run with runserver
Finally, you can run the site with this command:
`python3 manage.py runserver 0.0.0.0:8000`

It will run at port 8000, but you can change the port. It won't run with https in this mode, and it's generally not recommended to do this since you won't have access logs either.

Here, you can play with the Django admin panel. Just go to /admin on your instance and you can manage pretty much everything at a low level.

## Notes about configuration
By default, the site will...
* Use SQLite by default

The database is at `closedverse.sqlite3` by default. To change this, search `DATABASES` in settings.py. If you want to use MySQL, look up how to use it in a Django app. Too lazy for a tutorial for this at the moment. OK?
* Upload images locally to `media/`

As of writing, there's no way to use another image provider, such as Cloudinary (that has been stripped out because they suck). This may pose an issue if your VPS has a low bandwidth limit.
* Users' IPs will reflect Cloudflare's servers if you host behind Cloudflare.

If you use Cloudflare, **you should fix this.** Install `django-xff` with Pip, then uncomment the line starting with `xff.middleware`... in settings.py, and confirm if IPs are correct. It's easy to mess this up, so pay attention to this.

**Please, please read settings.py** for more information. You can even change the site's name through there.
# Run with Gunicorn
I recommend running the site via Gunicorn, since it's faster and supports access logs.

**NOTE:** Set `DEBUG = False` in settings.py before you do this, or else static assets won't work.
* Install Gunicorn: `python3 -m pip install gunicorn`
* Test it out: `python3 -m gunicorn closedverse.wsgi --bind 0.0.0.0:8000`

You can also substitute `python3 -m gunicorn` with just `gunicorn` if that works out for you. **Remember to use your venv if you have one set up.**

Now, let's run gunicorn automatically:
## Set up systemd service (Linux only)
AKA, how to run Closedverse automatically, on boot, with error and access logging.
* Make sure you're root, or use sudo when doing the following:
* Copy `gunicorn-closedverse.service` to `/etc/systemd/system`.
* Edit the file (`sudo nano /etc/systemd/system/gunicorn-closedverse.service`) and adjust it accordingly.
	* If you're using venv, make sure the PATH reflects it.
	* More importantly, change the user if you don't intend to run this as root, and change the path to the closedverse-video-support directory if it's not at the root of your home directory. `%h` is used as a standin for your home directory in systemd services.
	* Also adjust the port accordingly with the `bind` parameter. [Optionally enable SSL.](https://docs.gunicorn.org/en/stable/settings.html#ssl)
* Run `sudo systemctl daemon-reload`.
	* You will need to run this every time you change the .service file, or else the changes will not persist.
* Start the service with `sudo systemctl start gunicorn-closedverse`.
* View the status with `sudo systemctl status gunicorn-closedverse`.
If there's an error, this is when you will know.

If there's no problems, make the service run at bootup by running `sudo systemctl enable gunicorn-closedverse`.

**PROTIP:** optimize and adjust Gunicorn to your liking (**you can also enable SSL!**) by following [their settings page.](https://docs.gunicorn.org/en/stable/settings.html) Either add settings to the .service file or start using a conf file.

# Troubleshooting
TBD. File issues if any of this doesn't work (I'm at least 20% confident it won't), or if there's common issues I should document. Thanks!


# Copyright
Copyright 2017 Arian Kordi, all rights reserved to their respective owners. (Nintendo, Hatena Co Ltd.)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)

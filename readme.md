There is also shell script setup.sh basically it is just these instructions.
Either run setup.sh:
sudo su
chmod 777 setup.sh
./setup.sh

or install as follows:

Installing Django, Xvfb, Firefox, Python-pip, Selenium, Virtualenv, Httpie
==========================================================================
In home directory:
------------------
sudo su

apt-get update
apt-get install -y httpie
apt-get install -y python-pip
apt-get install -y firefox
apt-get install -y xvfb
pip install virtualenv

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales

virtualenv crystal_knows
tar -xzf crystal_knows.tar.gz -C ./crystal_knows/
source crystal_knows/bin/activate
cd crystal_knows
pip install django
pip install selenium
pip install djangorestframework
xvfb-run python manage.py runserver 0.0.0.0:80

Running Crystal Knows app
============================
*After unpacking everything, you can run like this:
    ~/crystal_knows/python manage.py runserver
    *this uses localhost IP and port 8000 http://127.0.0.1:8000
*To run on server using xvfb
    xvfb-run python manage.py runserver 0.0.0.0:80

Requests Using Httpie
======================
I have set up a server @104.196.48.55
GET Request:
http http://104.196.48.55/

POST Request:
http --json POST http://104.196.48.55/ first_name="Taylor" last_name="Swift"

Requests Using Curl
===================
POST Request:
curl -H "Content-Type: application/json" -X POST -d '{"first_name":"Taylor","last_name":"Swift"}' http://104.196.48.55/

GET Request:
curl http://104.196.48.55/

Making Requests on localhost
============================
http http://127.0.0.1:8000
curl http://127.0.0.1:8000

The script has been extensively tested using donald duck an 2 pop stars as inputs

Troubleshooting
===============
- I had a problem with the locale when setting it up on the server, that why this is included
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales

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

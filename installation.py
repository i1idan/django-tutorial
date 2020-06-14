## installation in ubuntu

#check python versions

python -V
python3 -V

#create directory for virtualenviroment

mkdir dev
cd dev
mkdir trydjango
cd trydjango

which python #see the python path is correct

#create virtualenv
virtualenv /dev/trydjango -p /usr/bin/python3.6

#activate virtual env
 source /dev/trydjango/bin/activate
 
 ## to avoid premission error
 $ sudo chown -R  parsa:parsa #username  /dev/trydjango

pip install django==2.0.7 ##verison


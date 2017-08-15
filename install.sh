# DON'T: clone the repository and then run the script, as it does that for you
mkdir T59
cd T59
git clone https://github.com/jrmann100/troop59.git
sudo pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r troop59/requirements.txt
python troop59/app.py

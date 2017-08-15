# Troop59 #
A Flask web server/site for BSA Marin Council Troop 59.

## Installation ##
Note: I've created an sh file with all the commands below listed, so you can just copy-paste the whole thing, but I'd recommend going step-by-step.
1. Create and enter project folder
```
mkdir T59
```
```
cd T59
```
2. Clone the repository
```
git clone https://github.com/jrmann100/troop59.git
```
3. Create virtual enviroment (If you don't have pip, or Python at that, installed, you may be a lost cause.)
```
sudo pip install virtualenv
```
```
virtualenv env
```
4. Activate virtual enviroment
```
source env/bin/activate
```
5. Install Python dependencies
```
pip install -r troop59/requirements.txt
```
6. Run web application!
```
python troop59/app.py
```

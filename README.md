# Troop59 #
A Flask web server/site for BSA Marin Council Troop 59.

## Installation ##
Note: I've created an sh file with all the commands below listed, so you can just copy-paste the whole thing __(DON'T: clone the repository and then run the script, as it does that for you)__, but I'd recommend just going step-by-step.
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

You can even do this in a [Cloud9 Workspace](http://c9.io "Cloud9"), changing the last line of `app.py` from `port=9001` to `port=8080` and following the instructions at https://docs.c9.io/docs/run-an-application, and try out the project from there like [in this example.](https://ide.c9.io/jrmann100/install-instruction-testing/ "My Example Workspace")

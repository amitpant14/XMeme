# !bin/bash

cd backend

# Setup DB or any other environment variables you want to setup.

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sleep 5
flask db init
flask db upgrade
flask run

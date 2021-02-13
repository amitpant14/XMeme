#!/bin/bash

cd backend


# Setup DB or any other environment variables you want to setup.

pip3 install -r requirements.txt

flask db init

flask db upgrade

flask run

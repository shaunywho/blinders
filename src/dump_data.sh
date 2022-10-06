#!/bin/bash

python3 manage.py dumpdata blinders.Profile  > ./fixtures/profile.json
python3 manage.py dumpdata blinders.User  > ./fixtures/user.json 

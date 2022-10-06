#!/bin/bash

python3 manage.py dumpdata blinders.Profile  > ./fixtures/profile.json
python3 manage.py dumpdata auth.User  > ./fixtures/user.json 

#!/bin/bash
yes | python3 manage.py flush
python3 manage.py loaddata fixtures/user.json 
python3 manage.py loaddata fixtures/profile.json

rm -r ./media/images/*
cp -r ./test_images/* media/images/

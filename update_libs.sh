#!/bin/bash

cp ../intrepid_release_x64/Release/intrepid_dll.dll libs/win64/
cp ../intrepid_release_x64/Release/_api.pyd libs/win64/
cp ../intrepid/src/api/api.py intrepyd
cp ../intrepid/src/api/Intrepid.h include

python setup.py install

coverage run -m unittest discover
coverage report


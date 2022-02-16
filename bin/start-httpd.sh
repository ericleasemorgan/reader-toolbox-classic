#!/usr/bin/env bash

pushd ../db_viewer_py
echo 'open web browser to http://localhost:8000'
python webserver.py
popd

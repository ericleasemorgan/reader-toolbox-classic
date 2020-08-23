#!/usr/bin/env bash

pushd ../db_viewer_py
open http://localhost:8000
python webserver.py
popd

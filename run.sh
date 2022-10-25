#!/bin/bash

# turn on bash's job control
set -m

# modify index.html file to add facebook pixel and google analytics
python ./src/demo.py

# Start streamlit server
python ./src/api.py &

# bring to front the last process
fg %
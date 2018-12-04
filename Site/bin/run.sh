#!/bin/bash
#
# Sanity check to test that we can render the base template
#
export FLASK_DEBUG=1
export FLASK_APP=tomhartung.py

cd .. && python3 -m flask run --port=5002

#!/bin/bash
export GO_SERVER_URL="http://localhost:8153"
export GO_SERVER_ADMIN_PASSWORD="admin"

if ! [ -d  venv ] ; then
  virtualenv venv
  source venv/bin/activate

  pip install -r requirements.txt
fi

source venv/bin/activate
python configuration.py

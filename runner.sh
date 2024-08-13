#!/bin/sh
source venv/bin/activate
cd erp && gunicorn erp.wsgi

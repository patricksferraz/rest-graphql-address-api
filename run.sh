#!/bin/bash

# POSTGRES ENV CONFIGS
export POSTGRES_URL="172.18.0.2"
export POSTGRES_USER="postgres"
export POSTGRES_PW="mysecretpass"
export POSTGRES_DB="address"

# FLASK ENV CONFIGS
# export FLASK_APP=api_rest.py
export FLASK_APP=api_graphql.py
export FLASK_ENV=development

echo "######################################"
echo "Up flask"
echo "######################################"
flask run

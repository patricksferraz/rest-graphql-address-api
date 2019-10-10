#!/bin/bash

# POSTGRES ENV CONFIGS
export POSTGRES_URL="172.18.0.2"
export POSTGRES_USER="postgres"
export POSTGRES_PW="mysecretpass"
export POSTGRES_DB="address"

# PGADMIN ENVS CONFIG
export PGADMIN_DE="postgres"
export PGADMIN_DP="mysecretpass"

# FLASK ENV CONFIGS
# export FLASK_APP=api_rest.py
export FLASK_APP=api_graphql.py
export FLASK_ENV=development


echo "######################################"
echo "Install docker"
echo "######################################"
# sudo pacman -Suy docker containerd --noconfirm

echo "######################################"
echo "Install python and pip"
echo "######################################"
sudo pacman -Suy python python-pip --noconfirm

echo "######################################"
echo "Install dependencies"
echo "######################################"
sudo pip install -rrequirements.txt

echo "######################################"
echo "Up postgresql and pgadmin4"
echo "######################################"
# docker network create \
#     -d bridge \
#     --subnet=172.18.0.0/16 postgres-network
# docker run \
#     --network=postgres-network \
#     --name postgres-address \
#     -e POSTGRES_USER=$POSTGRES_USER \
#     -e POSTGRES_PASSWORD=$POSTGRES_PW \
#     -e POSTGRES_DB=$POSTGRES_DB \
#     --ip 172.18.0.2 \
#     -d postgres
# docker run \
#     --network=postgres-network \
#     -p 80:80 \
#     -e PGADMIN_DEFAULT_EMAIL=$PGADMIN_DE \
#     -e PGADMIN_DEFAULT_PASSWORD=$PGADMIN_DP \
#     --ip 172.18.0.3 \
#     -d dpage/pgadmin4

sleep 5

echo "######################################"
echo "Populate postgresql"
echo "######################################"
# python db/generate.py \
#     -z db/tables \
#     -s db/struct_tables.json \
#     -t db/preprocessing

echo "######################################"
echo "Up flask"
echo "######################################"
flask run

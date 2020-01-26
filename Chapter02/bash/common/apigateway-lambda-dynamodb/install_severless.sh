#!/bin/bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

#import variables
. ./common_variables.sh

#Refresh your local package index
sudo apt update

# install required dependencies
sudo apt install build-essential apt-transport-https lsb-release ca-certificates curl -y

# If you want node version 12:
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

# Install Node.js from the repositories
sudo apt install nodejs -y

#Check the node version
nodejs -v

# Install the Node.js package manager
sudo apt install npm -y

# Check the version:
npm -v

# Install the serverless 
sudo npm install -g serverless

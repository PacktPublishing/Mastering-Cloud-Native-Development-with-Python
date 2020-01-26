
#!/bin/bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

#import variables
. ./common_variables.sh

#Refresh your local package index
sudo apt update

sudo pip3 install awscli --upgrade

aws --v
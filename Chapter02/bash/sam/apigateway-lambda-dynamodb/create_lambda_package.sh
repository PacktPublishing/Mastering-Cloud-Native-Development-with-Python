#!/bin/bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0
# This script creates a Zip package of the Lambda source files
# install sudo apt install zip

. ./common-variables.sh
sudo apt install zip -y
(mkdir -p ${SOURCE_BUILD_FOLDER}/${TEMPLATE};
mkdir -p ${TARGET_PACKAGE_FOLDER};
sudo rsync -avhH --include='*.py' --exclude="*.pyc" --exclude="__pycache__" ${LAMBDA_FOLDER}/ \
  ${SOURCE_BUILD_FOLDER}/${TEMPLATE} --delete --delete-excluded;
cd ${SOURCE_BUILD_FOLDER}/${TEMPLATE}; 
zip -rFS ../${ZIP_FILE} *;
ls -l ../${ZIP_FILE};)
cp  ${SOURCE_BUILD_FOLDER}/${ZIP_FILE} ${TARGET_PACKAGE_FOLDER}/${ZIP_FILE}


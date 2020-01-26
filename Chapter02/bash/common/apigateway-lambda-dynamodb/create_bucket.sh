#!/usr/bin/env bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

. ./common_variables.sh

aws s3api create-bucket --bucket ${BUCKET} --profile ${PROFILE} \
  --create-bucket-configuration LocationConstraint=${REGION} \
  --region ${REGION} --profile ${PROFILE}

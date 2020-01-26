#!/bin/sh
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

. ./common_variables.sh

endpoint=$(aws cloudformation describe-stacks --stack-name ${TEMPLATE} \
  --query 'Stacks[].Outputs[?OutputKey==`ServiceEndpoint`].OutputValue' \
  --output text --profile ${PROFILE} --region ${REGION})
echo ${endpoint}
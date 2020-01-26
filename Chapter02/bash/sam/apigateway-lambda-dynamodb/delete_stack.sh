#!/usr/bin/env bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

. ./common_variables.sh

aws cloudformation delete-stack --stack-name ${TEMPLATE} \
    --region ${REGION} --profile ${PROFILE}

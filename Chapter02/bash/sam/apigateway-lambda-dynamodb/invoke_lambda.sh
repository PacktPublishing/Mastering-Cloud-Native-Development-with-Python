#!/bin/sh
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

. ./common_variables.sh

status_code=$(aws lambda invoke --invocation-type Event --function-name ${FUNCTION_NAME} \
    --payload file://../../../sample_data/events/request-api-gateway-get-valid.json \
    outputfile.tmp --region ${REGION} --profile ${PROFILE})
echo "$status_code"
if echo "$status_code" | grep -q "202";
then 
    echo "pass"
    exit 0
else 
    exit 1
fi
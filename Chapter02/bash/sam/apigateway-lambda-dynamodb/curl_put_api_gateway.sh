#!/bin/sh
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

#endpoint="https://qzed4tz5q3.execute-api.eu-west-1.amazonaws.com/Prod/visits/324"
#endpoint="$(python3 get_apigateway_endpoint.py)"
endpoint=$(./get_api_endpoint.sh)
echo ${endpoint}
status_code=$(curl -i -H \"Accept: application/json\" -H \"Content-Type: application/json\" -X PUT ${endpoint} \
             -d '{"EventCount": 2, "EventDay": 20110624, "EventId": "324"}') 
             
echo "$status_code"
if echo "$status_code" | grep -q "\"HTTPStatusCode\": 200";
then 
    echo "pass"
    exit 0
else 
    echo "fail"
    exit 1
fi

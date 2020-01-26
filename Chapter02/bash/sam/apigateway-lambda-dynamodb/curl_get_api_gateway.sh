#!/bin/sh
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

endpoint=$(./get_api_endpoint.sh)/324
echo ${endpoint}
status_code=$(curl -i -H \"Accept: application/json\" -H \"Content-Type: application/json\" -X GET ${endpoint})
echo "$status_code"
if echo "$status_code" | grep -q "HTTP/2 200";
then 
    echo "pass"
    exit 0
else 
    echo "fail"
    exit 1
fi
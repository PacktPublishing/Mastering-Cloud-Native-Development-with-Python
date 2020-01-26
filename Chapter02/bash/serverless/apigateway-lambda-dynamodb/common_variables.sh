#!/bin/sh
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

export PROFILE="demo"
export REGION="eu-west-1"
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --profile ${PROFILE} | tr -d '\"')
# export aws_account_id="000000000000"
export TEMPLATE="lambda-dynamo-data-api-serverless-dev"
export BUCKET="testbucket121f"
export PREFIX="tmp/sam"
export SOURCE_BUILD_FOLDER=../../../build
export TARGET_PACKAGE_FOLDER=../../../package

#Lambda variables
export PYTHON_VERSION="python3.7"
export FUNCTION_NAME="lambda-dynamo-data-api-sam"
export LAMBDA_FOLDER=../../../lambda_dynamo_crud
export LAMBDA_FILE="lambda_return_dynamo_records.py"
export ZIP_FILE="lambda-dynamo-data-api.zip"
#!/usr/bin/env bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

#Variables
. ./common_variables.sh

#Create the roles needed by API Gateway and Lambda
# ./create-role.sh

#Create Zip file of your Lambda code (works on Windows and Linux) 
./create_lambda_package.sh

#Package your Serverless Stack using SAM + Cloudformation
aws cloudformation package --template-file ${TEMPLATE}.yaml \
  --output-template-file ${TARGET_PACKAGE_FOLDER}/${TEMPLATE}-output.yaml \
  --s3-bucket ${BUCKET} --s3-prefix backend \
  --region ${REGION} --profile ${PROFILE}

#Deploy your Serverless Stack using SAM + Cloudformation
aws cloudformation deploy --template-file ${TARGET_PACKAGE_FOLDER}/${TEMPLATE}-output.yaml \
  --stack-name ${TEMPLATE} --capabilities CAPABILITY_IAM \
  --parameter-overrides AccountId=${AWS_ACCOUNT_ID} \
    PythonVersion=${PYTHON_VERSION} FunctionName=${FUNCTION_NAME} \
  --region ${REGION} --profile ${PROFILE}
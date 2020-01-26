#!/bin/bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

#import variables
. ./common_variables.sh

#Create Lambda Role
role_name=lambda-dynamo-data-api
aws iam create-role --role-name ${role_name} \
    --assume-role-policy-document file://../../../IAM/assume-role-lambda.json \
    --region ${REGION} --profile ${PROFILE}
sleep 1

#Create and attach policies to role
declare -a policy_array=("dynamo-full-user-visits" "cloudwatch-write")

for policy in "${policy_array[@]}"
do
    echo "Creating and attaching policy ${policy} to role ${role_name}"
    aws iam create-policy --policy-name ${policy} \
        --policy-document file://../../../IAM/${policy}.json \
        --region ${REGION} --profile ${PROFILE}
    sleep 1
    role_policy_arn="arn:aws:iam::${AWS_ACCOUNT_ID}:policy/${policy}"
    aws iam attach-role-policy \
        --role-name "${role_name}" \
        --policy-arn "${role_policy_arn}"  \
        --region ${REGION} --profile ${PROFILE}
done

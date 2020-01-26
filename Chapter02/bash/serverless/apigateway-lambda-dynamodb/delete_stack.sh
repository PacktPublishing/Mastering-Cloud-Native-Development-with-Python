#!/usr/bin/env bash
# Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.
# Licensed under the Apache License, Version 2.0

. ./common_variables.sh

sls remove --aws-profile ${PROFILE} 

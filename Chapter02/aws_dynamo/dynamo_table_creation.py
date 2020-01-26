"""
Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0
or in the "license" file accompanying this file. This file is distributed
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing
permissions and limitations under the License.


Created on 8 Jan 2018

@author: Richard Freeman

pip install boto3

This package creates a new DynamoDb table with the specified read and write capacity

"""
import logging

import boto3

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)


def create_dynamo_lambda_counters_table(table_name_value, enable_streams=False,
                                        read_capacity=100,
                                        write_capacity=50,
                                        region='eu-west-1'):
    table_name = table_name_value
    logger.info('creating table: ' + table_name)
    try:
        client = boto3.client(service_name='dynamodb', region_name=region)
        logger.info(client.create_table(TableName=table_name,
                                        AttributeDefinitions=[{'AttributeName': 'EventId',
                                                         'AttributeType': 'S'},
                                                        {'AttributeName': 'EventDay',
                                                         'AttributeType': 'N'}],
                                        KeySchema=[{'AttributeName': 'EventId',
                                              'KeyType': 'HASH'},
                                             {'AttributeName': 'EventDay',
                                              'KeyType': 'RANGE'},
                                             ],
                                        ProvisionedThroughput={'ReadCapacityUnits': read_capacity,
                                                         'WriteCapacityUnits': write_capacity}))
    except Exception as e:
        logger.error(str(type(e)))
        logger.error(e.__doc__)
        logger.error(e)


def main():
    table_name = 'poc-lambda-user-visits'
    table_name = 'poc-lambda-user-visits-replicated'
    create_dynamo_lambda_counters_table(table_name, True, 1, 1)


if __name__ == '__main__':
    main()

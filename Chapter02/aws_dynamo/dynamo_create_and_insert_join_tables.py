"""
Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0
or in the "license" file accompanying this file. This file is distributed
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing
permissions and limitations under the License.


Created on 17 Mar 2019

@author: Richard Freeman

pip install boto3

This package creates two new DynamoDb table, loads data from a file and is
 used for testing a JOIN

"""
import time
import csv
import json
import logging

import boto3

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)


class DynamoRepository:
    def __init__(self, target_dynamo_table, region='eu-west-1'):
        self.dynamo_resource = boto3.resource(service_name='dynamodb',
                                              region_name='eu-west-1')
        self.target_dynamo_table = target_dynamo_table
        self.db_table = self.dynamo_resource.Table(self.target_dynamo_table)

    def insert_dynamo_row(self, insert_record):
        insert_record_parsed = {k: (int(v) if (v.isdigit() and k != 'EventId') else str(v))
                                for (k, v) in insert_record.items()}
        return self.db_table.put_item(Item=insert_record_parsed)


def create_dynamo_lambda_counters_table(table_name_value, enable_streams=False,
                                        read_capacity=100,
                                        write_capacity=50,
                                        range_definition={'AttributeName': 'EventDate',\
                                                          'AttributeType': 'N'},
                                        region='eu-west-1'):
    table_name = table_name_value
    logging.info('creating table: ' + table_name)
    try:
        client = boto3.client(service_name='dynamodb', region_name=region)
        logging.info(client.create_table(TableName=table_name,
                                         AttributeDefinitions=[{'AttributeName': 'EventId',
                                                         'AttributeType': 'S'},
                                                        range_definition],
                                         KeySchema=[{'AttributeName': 'EventId',
                                              'KeyType': 'HASH'},
                                             {'AttributeName': range_definition['AttributeName'],
                                              'KeyType': 'RANGE'},
                                             ],
                                         ProvisionedThroughput={'ReadCapacityUnits': read_capacity,
                                                         'WriteCapacityUnits': write_capacity}))
    except Exception as e:
        logging.error(str(type(e)))
        logging.error(e)


def insert_rows_into_table(table_name, input_data_path):
    dynamo_repo = DynamoRepository(table_name)
    with open(input_data_path, 'r') as sample_file:
        csv_reader = csv.DictReader(sample_file)
        for row in csv_reader:
            dynamo_repo.insert_dynamo_row(json.loads(json.dumps(row)))


def main():
    table_name = 'user-visits'
    range_definition = {'AttributeName': 'EventDay', 'AttributeType': 'N'}
    create_dynamo_lambda_counters_table(table_name, True, 1, 1, range_definition)
    time.sleep(20)
    input_data_path = '../sample_data/employee/dynamodb-sample-data.txt'
    insert_rows_into_table(table_name, input_data_path)

    table_name = 'event-table-details'
    range_definition = {'AttributeName': 'EventName', 'AttributeType': 'S'}
    create_dynamo_lambda_counters_table(table_name, True, 1, 1, range_definition)
    time.sleep(20)
    input_data_path = '../sample_data/employee/dynamodb-sample-data-event-details.txt'
    insert_rows_into_table(table_name, input_data_path)


if __name__ == '__main__':
    main()

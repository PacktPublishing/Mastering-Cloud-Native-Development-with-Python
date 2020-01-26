"""
Copyright (c) 2017-2020 STARWOLF Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0
or in the "license" file accompanying this file. This file is distributed
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing
permissions and limitations under the License.

Created on 30 Dec 2017
@author: Richard Freeman

This Lambda queries the remote DynamoDB for a specific partition and greater than a
specific sort key.

"""

from boto3 import resource
from boto3.dynamodb.conditions import Key


class DynamoRepository:
    def __init__(self, table_name):
        self.dynamo_client = resource(service_name='dynamodb',
                                      region_name='eu-west-1')
        self.table_name = table_name
        self.db_table = self.dynamo_client.Table(table_name)

    def query_by_entityid_date(self, entity_id, entity_date):
        partition_key = 'EventId'
        partition_value = entity_id
        sort_key = 'EventDay'
        sort_value = entity_date
        response = self.db_table.query(KeyConditionExpression=
                                       Key(partition_key).eq(partition_value)
                                       & Key(sort_key).gte(sort_value))
        return response.get('Items')

    def query_by_entityid(self, entity_id):
        partition_key = 'EventId'
        partition_value = entity_id
        response = self.db_table.query(KeyConditionExpression=
                                       Key(partition_key).eq(partition_value))
        return response.get('Items')

    def insert_event(self, event_data):
        return self.db_table.put_item(Item=event_data)

    def update_event_counter(self, event_data):
        return self.db_table.update_item(
            Key={
                'EventId': event_data.get('EventId'),
                'EventDay': event_data.get('EventDay')
            },
            ExpressionAttributeValues={":eventCount": int(event_data.get('EventCount', 1))},
            UpdateExpression="ADD EventCount :eventCount",
            ReturnValues='ALL_NEW')

    def delete_event(self, event_data):
        return self.db_table.delete_item(Key={
            'EventId': event_data.get('EventId'),
            'EventDay': event_data.get('EventDay')},
            ReturnValues='ALL_OLD')



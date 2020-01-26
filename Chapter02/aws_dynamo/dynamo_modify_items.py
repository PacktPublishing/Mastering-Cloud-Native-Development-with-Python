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

This packages inserts records into DynamoDB

"""

import logging

from boto3 import resource

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)


class DynamoRepository:
    def __init__(self, target_dynamo_table, region='eu-west-1'):
        self.dynamodb = resource(service_name='dynamodb', region_name=region)
        self.target_dynamo_table = target_dynamo_table
        self.db_table = self.dynamodb.Table(self.target_dynamo_table)

    def update_dynamo_event_counter(self, event_name, event_datetime, event_count=1):
        return self.db_table.update_item(
            Key={
                'EventId': event_name,
                'EventDay': event_datetime
            },
            ExpressionAttributeValues={":eventCount": event_count},
            UpdateExpression="ADD EventCount :eventCount")

    def insert_dynamo_event(self, event_data):
        response = self.db_table.put_item(Item=event_data)
        return response


def main():
    table_name = 'user-visits-sam'
    dynamo_repo = DynamoRepository(table_name)
    """
    logger.info(dynamo_repo.update_dynamo_event_counter('324', 20171001, 1))
    logger.info(dynamo_repo.update_dynamo_event_counter('324', 20171001, 2))
    logger.info(dynamo_repo.update_dynamo_event_counter('324', 20171002, 5))
    """
    logger.info(dynamo_repo.insert_dynamo_event({'EventId':'324',
                                                 'EventDay': 20171001,
                                                 'EventCount': 100}))


if __name__ == '__main__':
    main()

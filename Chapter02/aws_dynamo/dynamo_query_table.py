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
This package is used to query DynamoDB
"""
import logging
import decimal
import json

from boto3 import resource
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class DynamoRepository:
    def __init__(self, target_dynamo_table, region='eu-west-1'):
        self.dynamodb = resource(service_name='dynamodb', region_name=region)
        self.dynamo_table = target_dynamo_table
        self.db_table = self.dynamodb.Table(self.dynamo_table)

    def query_dynamo_record_by_parition(self, parition_key, parition_value):
        try:
            response = self.db_table.query(
                KeyConditionExpression=Key(parition_key).eq(parition_value))
            for record in response.get('Items'):
                logger.info(json.dumps(record, cls=DecimalEncoder))
            return

        except Exception as e:
            logger.info(e.__doc__)
            logger.info(e)

    def query_dynamo_record_by_parition_sort_key(self, parition_key, parition_value,
                                                 sort_key, sort_value):
        try:
            response = self.db_table.query(
                KeyConditionExpression=Key(parition_key).eq(parition_value)
                                       & Key(sort_key).gte(sort_value))
            for record in response.get('Items'):
                logger.info(json.dumps(record, cls=DecimalEncoder))
            return

        except Exception as e:
            logger.error(e.__doc__)
            logger.error(e)


def main():
    table_name = 'user-visits-sam'
    parition_key = 'EventId'
    parition_value = '324'
    sort_key = 'EventDay'
    sort_value = 20171014

    dynamo_repo = DynamoRepository(table_name)
    logger.info('Reading all data for user:%s' % parition_value)
    dynamo_repo.query_dynamo_record_by_parition(parition_key, parition_value)

    logger.info('Reading all data for user:%s with date > %d' % (parition_value, sort_value))
    dynamo_repo.query_dynamo_record_by_parition_sort_key(parition_key,
                                                         parition_value,
                                                         sort_key,
                                                         sort_value)


if __name__ == '__main__':
    main()

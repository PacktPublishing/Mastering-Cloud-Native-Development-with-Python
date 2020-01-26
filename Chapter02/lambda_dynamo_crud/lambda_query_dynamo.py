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
import json
import logging
import os

try:
    import dynamo_repository
except ImportError:
    from lambda_dynamo_crud import dynamo_repository

try:
    import http_utils
except ImportError:
    from lambda_dynamo_crud import http_utils

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)


def print_exception(e):
    logger.error(''.join(['Exception ', str(type(e))]))
    logger.error(''.join(['Exception ', str(e.__doc__)]))
    logger.error(''.join(['Exception ', str(e)]))


class Controller():
    def __init__(self):
        pass

    @staticmethod
    def process_dynamo_records(event):
        try:
            http_method = event['httpMethod'].lower()
            validation_result = http_utils.HttpUtils.parse_parameters(event)
            parsed_body = http_utils.HttpUtils.parse_body(event)
            if http_method == 'get':
                if validation_result.get('parsedParams', None) is None:
                    return http_utils.HttpUtils.respond(err=validation_result['err'], err_code=404)
                resource_id = str(validation_result['parsedParams']["resource_id"])
                if validation_result['parsedParams'].get("startDate") is None:
                    result = repo.result = repo.query_by_entityid(entity_id=resource_id)
                else:
                    start_date = int(validation_result['parsedParams']["startDate"])
                    result = repo.query_by_entityid_date(entity_id=resource_id,
                                                         entity_date=start_date)
            elif http_method == 'delete':
                if parsed_body['err'] is None:
                    if parsed_body['body'].get('EventId', '') != '':
                        result = repo.delete_event(parsed_body['body'])
                    else:
                        return http_utils.HttpUtils.respond(err=Exception('Missing EventId'),
                                                            err_code=404,
                                                            res=json.dumps(parsed_body['body']))
            elif http_method == 'post':

                if parsed_body['err'] is None:
                    if parsed_body['body'].get('EventId', '') != '':
                        result = repo.update_event_counter(parsed_body['body'])
                    else:
                        return http_utils.HttpUtils.respond(err=Exception('Missing EventId'),
                                                            err_code=404,
                                                            res=json.dumps(parsed_body['body']))
                else:
                    return http_utils.HttpUtils.respond(parsed_body['err'], "Error processing request")
            elif http_method == 'put':
                if parsed_body['err'] is None:
                    if parsed_body['body'].get('EventId', '') != '':
                        result = repo.insert_event(parsed_body['body'])
                    else:
                        return http_utils.HttpUtils.respond(err=Exception('Missing EventId'),
                                                            err_code=404,
                                                            res=json.dumps(parsed_body['body']))
                else:
                    return http_utils.HttpUtils.respond(parsed_body['err'], "Error processing request")

            return http_utils.HttpUtils.respond(res=result)

        except Exception as e:
            print_exception(e)
            return http_utils.HttpUtils.respond(err=e, err_code=404)


table_name_global = os.getenv('DYNAMO_TABLE_NAME')
if table_name_global is None:
    table_name_global = 'user-visits-serverless' #'user-visits-sam'
repo = dynamo_repository.DynamoRepository(table_name=table_name_global)


def lambda_handler(event, context):
    response = Controller.process_dynamo_records(event)
    return response

"""
Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). 
You may not use this file except in compliance with the License. 
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0
or in the "license" file accompanying this file. This file is distributed 
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
express or implied. See the License for the specific language governing 
permissions and limitations under the License.

Created on 31 Dec 2017

@author: Richard Freeman

"""
import logging
import json

try:
    import lambda_query_dynamo
except ModuleNotFoundError:
    from lambda_dynamo_crud import ambda_query_dynamo

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


with open('../sample_data/events/request-api-gateway-delete-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-put-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-error.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-post-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-post-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-get-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-get-valid-date.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-get-invalid-no-date.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info('Response: %s\n' % json.dumps(response))

with open('../sample_data/events/request-api-gateway-error.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info("Response: %s\n" % json.dumps(response))

with open('../sample_data/events/request-api-gateway-delete-valid.json', 'r') as sample_file:
    event = json.loads(sample_file.read())
logger.info(sample_file.name.split('/')[-1])
logger.info("Using data: " + str(event))
response = lambda_query_dynamo.lambda_handler(event, None)
logger.info("Response: %s\n" % json.dumps(response))
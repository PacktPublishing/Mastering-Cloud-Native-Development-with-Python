"""
Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0
or in the "license" file accompanying this file. This file is distributed
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing
permissions and limitations under the License.

Lambda DynamoDB unit tests

"""

import unittest
import json

try:
    import lambda_query_dynamo
except ModuleNotFoundError:
    from lambda_dynamo_crud import lambda_query_dynamo
try:
    import http_utils
except ModuleNotFoundError:
    from lambda_dynamo_crud import http_utils


class TestIndexGetMethod(unittest.TestCase):
    def setUp(self):
        self.valid_json_event_with_date = json.loads('{"queryStringParameters": {"startDate": "20171013"},'
                                        '"httpMethod": "GET","path": "/path/to/resource/324","headers": '
                                        'null} ')

        self.valid_json_event_without_date = json.loads('{"queryStringParameters": {},'
                                                     '"httpMethod": "GET","path": "/path/to/resource/324","headers": '
                                                     'null} ')

        self.invalidJsonResourceData = json.loads('{"queryStringParameters": {"startDate": "20171013"},'
                                                '"httpMethod": "GET","path": "/path/to/resource/324f","headers": '
                                                'null} ')

        self.invalidJsonData = "{ invalid JSON request!} "

    def tearDown(self):
        pass

    def test_validparameters_parseparameters_pass(self):
        parameters = http_utils.HttpUtils.parse_parameters(self.valid_json_event_without_date)
        assert parameters['parsedParams']['resource_id'] == u'324'

    def test_validparameterswithdate_parseparameters_pass(self):
        parameters = http_utils.HttpUtils.parse_parameters(self.valid_json_event_with_date)
        assert parameters['parsedParams']['startDate'] == u'20171013'
        assert parameters['parsedParams']['resource_id'] == u'324'

    def test_invalidjson_getrecord_notfound404(self):
        result = lambda_query_dynamo.Controller.process_dynamo_records(self.invalidJsonData)
        assert result['statusCode'] == '404'

    def test_invaliduserid_getrecord_invalididerror(self):
        result = lambda_query_dynamo.Controller.process_dynamo_records(self.invalidJsonResourceData)
        assert result['statusCode'] == '404'
        assert json.loads(result['body'])['message'] == "resource_id not a number"

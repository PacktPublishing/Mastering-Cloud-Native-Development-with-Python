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
import decimal


class HttpUtils:
    def __init__(self):
        pass

    @staticmethod
    def parse_parameters(event):
        try:
            return_parameters = event['queryStringParameters'].copy()
        except Exception:
            return_parameters = {}
        try:
            resource_id = event.get('path', '').split('/')[-1]
            if resource_id.isdigit():
                return_parameters['resource_id'] = resource_id
            else:
                return {"parsedParams": None, "err":
                    Exception("resource_id not a number")}
        except Exception as e:
            return {"parsedParams": None, "err": e}  
            # Generally bad idea to expose exceptions
        return {"parsedParams": return_parameters, "err": None}

    @staticmethod
    def respond(err=None, err_code=400, res=None):
        return {
            'statusCode': str(err_code) if err else '200',
            'body': '{"message":%s}' % json.dumps(str(err)) if err else
            json.dumps(res, cls=DecimalEncoder),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }

    @staticmethod
    def parse_body(event):
        try:
            return {"body": json.loads(event['body']), "err": None}
        except Exception as e:
            return {"body": None, "err": e}


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
